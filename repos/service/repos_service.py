from abc import ABC, abstractmethod


class ReposService(ABC):
    @abstractmethod
    def save(self, accountId, accessToken):
        pass

    @abstractmethod
    def list(self, accountId):
        pass