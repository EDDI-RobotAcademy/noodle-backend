from account.repository.account_repostiory_impl import AccountRepositoryImpl
from branches.repository.branches_repository_impl import BranchesRepositoryImpl
from commits.repository.commits_repository_impl import CommitsRepositoryImpl
from commits.service.commits_service import CommitsService
from repos.repository.repos_repository_impl import ReposRepositoryImpl


class CommitsServiceImpl(CommitsService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__commitsRepository = CommitsRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__reposRepository = ReposRepositoryImpl.getInstance()
            cls.__instance.__branchesRepository = BranchesRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def save(self, accountId, accessToken, reponame, branchname):
        account = self.__accountRepository.findAccountByAccountId(account_id=accountId)
        repo = self.__reposRepository.getRepository(account, reponame)
        branch = self.__branchesRepository.getBranch(branchname, repo)
        self.__commitsRepository.saveCommits(account, accessToken, repo, branch)

    def list(self, accountId, reponame, branchname, page):
        account = self.__accountRepository.findAccountByAccountId(account_id=accountId)
        repo = self.__reposRepository.getRepository(account, reponame)
        branch = self.__branchesRepository.getBranch(branchname, repo)

        return self.__commitsRepository.getAllCommits(account, branch, page)
