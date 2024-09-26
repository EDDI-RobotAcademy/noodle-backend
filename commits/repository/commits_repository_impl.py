import requests
import re

from django.utils.dateparse import parse_time

from commits.entity.models import Commits
from commits.repository.commits_repository import CommitsRepository


class CommitsRepositoryImpl(CommitsRepository):
    __instance = None
    GITHUB_API_URL = "https://api.github.com"
    PER_PAGE = 8

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def saveCommits(self, account, accessToken, repo, branch):
        latestCommits = Commits.objects.filter(branch=branch).order_by('-commit_date').first()

        getRepositoryUrl = self.GITHUB_API_URL + f"/repos/{account.username}/{repo.name}/commits"
        headers = {
            'Authorization': f'Bearer {accessToken}'
        }
        params = {
            "sha": branch.name,
            "per_page": 10,
            "page": 1,
            "since": latestCommits.time.isoformat() if latestCommits else None
        }
        response = requests.get(getRepositoryUrl, headers=headers, params=params)

        resHeaders = response.headers
        link = resHeaders['Link']
        pattern = re.search(r'page=(\d+)>; rel="last"', link)

        lastPageNumber = int(pattern.group(1))
        for page in range(1, lastPageNumber):
            params = {
                "sha": branch.name,
                "per_page": 10,
                "page": page,
                "since": latestCommits.time.isoformat() if latestCommits else None
            }
            response = requests.get(getRepositoryUrl, headers=headers, params=params)
            commits = response.json()

            for commit in commits:
                message = commit['commit']['message']
                author = commit['author']['name']
                commitTime = parse_time(commit['author']['date'])
                Commits.objects.get_or_create(message=message, author=author, time=commitTime, branch=branch)

    def getPagedCommits(self, account, branch, page):
        return Commits.objects.filter(account=account, name=branch).order_by("-time")[self.PER_PAGE * (page - 1):self.PER_PAGE * page]
