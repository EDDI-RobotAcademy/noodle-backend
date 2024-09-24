from repos.repository.repos_repository_impl import ReposRepositoryImpl
from repos.service.repos_service import ReposService


class ReposServiceImpl(ReposService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__reposRepository = ReposRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self, username, accessToken):
        repos = self.__reposRepository.getAllRepositories(username, accessToken)

        repoList = []
        for repo in repos:
            repoList.append(repo['name'])

        return repoList


