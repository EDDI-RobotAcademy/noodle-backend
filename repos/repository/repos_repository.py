from abc import ABC, abstractmethod


class ReposRepository(ABC):
    @abstractmethod
    def getAllRepositories(self, username, accessToken):
        pass