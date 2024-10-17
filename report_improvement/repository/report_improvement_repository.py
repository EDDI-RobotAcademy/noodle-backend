from abc import abstractmethod, ABC


class ResultReportImprovementRepository(ABC):
    @abstractmethod
    def createResultReportImprovement(self, report):
        pass