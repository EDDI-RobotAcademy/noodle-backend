import requests

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

    def getAllRepositories(self, username, accessToken):
        getGithubRepositoryUrl = self.GITHUB_API_URL + f"/users/{username}/repos?per_page=500"
        headers = {
            'Authorization': f'Bearer {accessToken}'
        }
        response = requests.get(getGithubRepositoryUrl, headers=headers)
        print("response:", response)

        return response.json()
