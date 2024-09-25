from abc import ABC, abstractmethod


class ReposService(ABC):
    @abstractmethod
    def save(self, accountId, accessToken):
        pass