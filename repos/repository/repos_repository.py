from abc import ABC, abstractmethod


class ReposRepository(ABC):
    @abstractmethod
    def getAllRepositories(self, account, accessToken):
        pass

    @abstractmethod
    def getRepository(self, account, reponame):
        pass