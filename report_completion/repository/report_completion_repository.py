from abc import abstractmethod, ABC


class ResultReportCompletionRepository(ABC):
    @abstractmethod
    def createResultReportCompletion(self, report):
        pass
