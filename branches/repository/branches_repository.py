from abc import ABC, abstractmethod


class BranchesRepository(ABC):
    @abstractmethod
    def getAllBranches(self, username, accessToken, reponame):
        pass