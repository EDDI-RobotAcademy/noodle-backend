from account.repository.account_repostiory_impl import AccountRepositoryImpl
from repos.repository.repos_repository_impl import ReposRepositoryImpl
from repos.service.repos_service import ReposService


class ReposServiceImpl(ReposService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__reposRepository = ReposRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self, accountId, accessToken):
        account = self.__accountRepository.findAccountByAccountId(id=accountId)
        repoList = self.__reposRepository.getAllRepositories(account, accessToken)

        return repoList
