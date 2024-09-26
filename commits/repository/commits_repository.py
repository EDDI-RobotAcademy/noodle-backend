from abc import ABC, abstractmethod


class CommitsRepository(ABC):
    @abstractmethod
    def saveCommits(self, account, accessToken, repo, branch):
        pass

    @abstractmethod
    def getPagedCommits(self, account, branch, page):
        pass