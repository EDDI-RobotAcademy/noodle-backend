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

    def save(self, accountId, accessToken):
        account = self.__accountRepository.findAccountByAccountId(accountId)
        self.__reposRepository.saveRepositories(account, accessToken)

    def list(self, accountId):
        account = self.__accountRepository.findAccountByAccountId(accountId)
        repos = self.__reposRepository.getAllRepositories(account)
        repoList = [repo.name for repo in repos]

        return repoList
