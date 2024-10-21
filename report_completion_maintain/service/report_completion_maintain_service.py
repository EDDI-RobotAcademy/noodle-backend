from abc import abstractmethod, ABC


class ResultReportCompletionMaintainService(ABC):
    @abstractmethod
    def create(self, resultReportId, score, detail):
        pass