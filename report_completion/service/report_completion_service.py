from abc import abstractmethod, ABC


class ResultReportCompletionService(ABC):
    @abstractmethod
    def create(self, resultReportId):
        pass