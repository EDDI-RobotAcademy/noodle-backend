from abc import ABC, abstractmethod


class BranchesRepository(ABC):
    @abstractmethod
    def getAllBranches(self, account, accessToken, reponame):
        pass

    @abstractmethod
