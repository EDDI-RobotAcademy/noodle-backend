from abc import abstractmethod, ABC


class BranchesService(ABC):
    @abstractmethod
    def list(self, username, accessToken, reponame):
        pass