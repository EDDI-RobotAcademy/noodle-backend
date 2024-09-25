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
        commitList = []

        commits, lastPageNumber = self.__commitsRepository.getCommitsOfPage(username, accessToken, reponame, branchname, pageNumber)

        for commit in commits:
            commitList.append(commit['commit']['message'])

        for page in range(2, lastPageNumber + 1):
            commits = self.__commitsRepository.getCommitsOfPage(username, accessToken, reponame, branchname, page)

            for commit in commits:
                commitList.append(commit['commit']['message'])

        return commitList
