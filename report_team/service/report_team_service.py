from abc import abstractmethod, ABC

class ResultReportTeamService(ABC):
    @abstractmethod
    def createResultReportTeamService(self, resultReportId):
        pass