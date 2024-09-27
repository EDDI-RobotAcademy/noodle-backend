from abc import ABC, abstractmethod


class CommitsService(ABC):
    @abstractmethod
    def save(self, accountId, accessToken, reponame, branchname):
        pass

    # @abstractmethod
    # def list(self, accountId, reponame, branchname, page):
    #     pass
    @abstractmethod
    def list(self, accountId, reponame, branchname):
        pass