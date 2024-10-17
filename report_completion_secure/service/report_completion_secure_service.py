from abc import abstractmethod, ABC


class ResultReportCompletionSecureService(ABC):
    @abstractmethod
    def create(self, resultReportId, score, detail):
        pass