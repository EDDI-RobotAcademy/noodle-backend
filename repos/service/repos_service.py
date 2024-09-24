from abc import ABC, abstractmethod


class ReposService(ABC):
    @abstractmethod
    def list(self, username, accessToken):
        pass