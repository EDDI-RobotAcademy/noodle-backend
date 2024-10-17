from abc import abstractmethod, ABC


class ResultReportImprovementContentRepository(ABC):
    @abstractmethod
    def createResultReportImprovementContent(self, report, content):
        pass