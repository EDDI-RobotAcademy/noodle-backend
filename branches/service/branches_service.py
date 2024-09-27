from abc import abstractmethod, ABC


class BranchesService(ABC):
    @abstractmethod
    def save(self, accountId, accessToken, reponame):
        pass

    @abstractmethod
    def list(self, accountId, reponame):
        pass