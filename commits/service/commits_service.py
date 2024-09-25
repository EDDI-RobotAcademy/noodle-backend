from abc import ABC, abstractmethod


class CommitsService(ABC):
    @abstractmethod
    def list(self, username, accessToken, reponame, branchname):
        pass