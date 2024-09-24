import requests

from commits.repository.commits_repository import CommitsRepository


class CommitsRepositoryImpl(CommitsRepository):
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

    def getCommitsOfPage(self, username, accessToken, reponame, branchname, pageNumber):
        getRepositoryUrl = self.GITHUB_API_URL + f"/repos/{username}/{reponame}/commits?sha={branchname}&per_page=20&page={pageNumber}"
        headers = {
            'Authorization': f'Bearer {accessToken}'
        }
        response = requests.get(getRepositoryUrl, headers=headers)
        print("response:", response)

        return response.json()
