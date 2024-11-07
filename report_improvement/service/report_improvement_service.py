from abc import abstractmethod, ABC


class ResultReportImprovementService(ABC):
    @abstractmethod
    def create(self, resultReportId):
        pass