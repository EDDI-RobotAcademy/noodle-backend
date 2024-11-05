from abc import abstractmethod, ABC


class ResultReportCompletionMaintainRepository(ABC):
    @abstractmethod
    def createResultReportCompletionMaintain(self, completion, score, detail):
        pass

    @abstractmethod
    def getResultReportCompletionMaintainByResultReportCompletion(self, completion):
        pass

    @abstractmethod
    def delete(self, completionObj):
        pass
