from branches.repository.branches_repository_impl import BranchesRepositoryImpl
from branches.service.branches_service import BranchesService


class BranchesServiceImpl(BranchesService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__branchesRepository = BranchesRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self, username, accessToken, reponame):
        branches = self.__branchesRepository.getAllBranches(username, accessToken, reponame)
        branchList = []
        for branch in branches:
            branchList.append(branch["name"])

        return branchList
