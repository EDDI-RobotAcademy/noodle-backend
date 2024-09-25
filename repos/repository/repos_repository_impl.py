import requests

from repos.entity.models import Repos
from repos.repository.repos_repository import ReposRepository


class ReposRepositoryImpl(ReposRepository):
    __instance = None
    GITHUB_API_URL = "https://api.github.com"

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getAllRepositories(self, account, accessToken):
        getGithubRepositoryUrl = self.GITHUB_API_URL + f"/users/{account.username}/repos?per_page=500"
        headers = {
            'Authorization': f'Bearer {accessToken}'
        }
        response = requests.get(getGithubRepositoryUrl, headers=headers)
        print("response:", response)

        repoList = [repo['name'] for repo in response.json()]
        print("repoList:", repoList)

        for repo in repoList:
            Repos.objects.get_or_create(name=repo, account=account)

        return repoList

