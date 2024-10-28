from abc import abstractmethod, ABC


class ResultReportTeamRepository(ABC):
    @abstractmethod
    def create(self, resultReport):
        pass

    @abstractmethod
    def getResultReportTeamByResultReport(self, report):
        pass