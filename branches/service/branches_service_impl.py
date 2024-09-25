from account.repository.account_repostiory_impl import AccountRepositoryImpl
from branches.repository.branches_repository_impl import BranchesRepositoryImpl
from branches.service.branches_service import BranchesService
from repos.repository.repos_repository_impl import ReposRepositoryImpl


class BranchesServiceImpl(BranchesService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__branchesRepository = BranchesRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__reposRepository = ReposRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self, accountId, accessToken, reponame):
        account = self.__accountRepository.findAccountByAccountId(account_id=accountId)
        repos = self.__reposRepository.getRepository(account=account, reponame=reponame)
        branchList = self.__branchesRepository.getAllBranches(account, accessToken, repos)

        return branchList
