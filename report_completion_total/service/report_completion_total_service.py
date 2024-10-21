from abc import abstractmethod, ABC

class ResultReportCompletionTotalService(ABC):
    @abstractmethod
    def create(self, resultReportId, score, detail):
        pass
