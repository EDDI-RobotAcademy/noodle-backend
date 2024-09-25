from abc import ABC, abstractmethod


class ReposRepository(ABC):
    @abstractmethod
    def saveRepositories(self, account, accessToken):
        pass

    @abstractmethod
    def getRepository(self, account, reponame):
        pass