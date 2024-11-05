from abc import abstractmethod, ABC


class ResultReportCompletionRepository(ABC):
    @abstractmethod
    def getResultRepositoryCompletionByResultReport(self, report):
        pass

    @abstractmethod
    def createResultReportCompletion(self, report):
        pass

    @abstractmethod
    def delete(self, report):
        pass
