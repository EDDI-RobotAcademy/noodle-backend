from abc import abstractmethod, ABC


class ResultReportCompletionMaintainRepository(ABC):
    @abstractmethod
    def createResultReportCompletionMaintain(self, completion, score, detail):
        pass