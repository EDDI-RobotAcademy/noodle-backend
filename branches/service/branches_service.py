from abc import abstractmethod, ABC


class BranchesService(ABC):
    @abstractmethod
    def list(self, accountId, accessToken, reponame):
        pass