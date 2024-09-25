from abc import ABC, abstractmethod


class CommitsRepository(ABC):
    @abstractmethod
    def getCommitsOfPage(self, username, accessToken, reponame, branchname, pageNumber):
        pass
