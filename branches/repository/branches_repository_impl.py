import requests

from branches.repository.branches_repository import BranchesRepository


class BranchesRepositoryImpl(BranchesRepository):
    __instance = None
    GITHUB_API_URL = "http://api.github.com"

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getAllBranches(self, username, accessToken, reponame):
        getRepositoryBranchesUrl = self.GITHUB_API_URL + f"/repos/{username}/{reponame}/branches?per_page=100"
        headers = {
            'Authorization': f'Bearer {accessToken}'
        }

        response = requests.get(getRepositoryBranchesUrl, headers=headers)
        print("response:", response)

        return response.json()
