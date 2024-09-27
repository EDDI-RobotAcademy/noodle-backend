import requests
import re

from django.utils.dateparse import parse_time
from datetime import datetime

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
        latestCommits = Commits.objects.filter(branch=branch).order_by('-time').first()

        getRepositoryUrl = self.GITHUB_API_URL + f"/repos/{account.username}/{repo.name}/commits"
        headers = {
            'Accept': "application/vnd.github+json",
            'Authorization': f'Bearer {accessToken}'
        }
        params = {
            "sha": branch.name,
            "since": latestCommits.time.isoformat() if latestCommits else None,
            "per_page": 1,
            "page": 1
        }
        response = requests.get(getRepositoryUrl, headers=headers, params=params)
        # print("response:", response.json())
        link = response.headers['Link']
        print("link:", link)
        pattern = re.search(r'page=(\d+)>; rel="last"', link)

        lastPageNumber = int(pattern.group(1))
        print("lastPageNumber:", lastPageNumber)
        for page in range(1, lastPageNumber+1):
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
                author = commit['author']['login']
                commitTime = parse_time(commit['commit']['author']['date'])

                Commits.objects.get_or_create(message=message, author=author, time=commit['commit']['author']['date'], branch=branch)

    # def getPagedCommits(self, account, branch, page):
    #     return Commits.objects.filter(account=account, name=branch).order_by("-time")[self.PER_PAGE * (page - 1):self.PER_PAGE * page]
    def getAllCommits(self, account, branch):
        return Commits.objects.filter(author=account.username, branch=branch).order_by("-time")

