from abc import ABC, abstractmethod


class CommitsService(ABC):
    @abstractmethod
    def save(self, accountId, accessToken, reponame, branchname):
        pass