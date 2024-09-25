from abc import ABC, abstractmethod


class ReposService(ABC):
    @abstractmethod
    def list(self, accountId, accessToken):
        pass