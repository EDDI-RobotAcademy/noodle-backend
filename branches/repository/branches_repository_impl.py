import requests

from branches.entity.models import Branches
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

    def getAllBranches(self, account, accessToken, repos):
        getRepositoryBranchesUrl = self.GITHUB_API_URL + f"/repos/{account.username}/{repos.name}/branches?per_page=100"
        headers = {
            'Authorization': f'Bearer {accessToken}'
        }

        response = requests.get(getRepositoryBranchesUrl, headers=headers)
        print("response:", response)

        branchList = [branch['name'] for branch in response.json()]
        print("branchList:", branchList)

        for branch in branchList:
            Branches.objects.get_or_create(name=branch, repos=repos)

        return branchList

    def getBranch(self, name, repos):
        return Branches.objects.get(name=name, repos=repos)
