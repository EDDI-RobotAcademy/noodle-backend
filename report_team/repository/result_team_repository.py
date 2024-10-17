from abc import abstractmethod, ABC


class ResultReportTeamRepository(ABC):
    @abstractmethod
    def getResultTeamById(self, id):
        pass

    @abstractmethod
    def create(self, resultReportId):
        pass