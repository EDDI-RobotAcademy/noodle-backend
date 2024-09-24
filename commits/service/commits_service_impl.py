from commits.repository.commits_repository_impl import CommitsRepositoryImpl
from commits.service.commits_service import CommitsService


class CommitsServiceImpl(CommitsService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__commitsRepository = CommitsRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self, username, accessToken, reponame, branchname, pageNumber):
        commits = self.__commitsRepository.getCommitsOfPage(username, accessToken, reponame, branchname, pageNumber)
        commitList = []
        for commit in commits:
            commitList.append(commit['commit']['message'])

        return commitList
