from abc import ABC, abstractmethod


class BranchesRepository(ABC):
    @abstractmethod
    def saveBranches(self, account, accessToken, reponame):
        pass

    @abstractmethod
    def getBranch(self, name, repos):
        pass

    @abstractmethod
    def getBranches(self, repos):
        pass