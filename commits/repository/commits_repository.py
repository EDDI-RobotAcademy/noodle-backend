from abc import ABC, abstractmethod


class CommitsRepository(ABC):
    @abstractmethod
    def saveCommits(self, account, accessToken, repo, branch):
        pass
