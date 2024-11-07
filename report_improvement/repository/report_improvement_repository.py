from abc import abstractmethod, ABC


class ResultReportImprovementRepository(ABC):
    @abstractmethod
    def createResultReportImprovement(self, report):
        pass

    @abstractmethod
    def getResultReportImprovement(self, report):
        pass

    @abstractmethod
    def delete(self, report):
        pass
