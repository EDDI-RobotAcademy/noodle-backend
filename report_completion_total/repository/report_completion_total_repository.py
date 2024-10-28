from abc import abstractmethod, ABC

class ResultReportCompletionTotalRepository(ABC):
    @abstractmethod
    def createResultReportCompletionTotal(self, completion, score, detail):
        pass

    @abstractmethod
    def getResultReportCompletionTotalByResultReportCompletion(self, completion):
        pass