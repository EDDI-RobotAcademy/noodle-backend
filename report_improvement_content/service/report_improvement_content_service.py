from abc import abstractmethod, ABC


class ResultReportImprovementContentService(ABC):
    @abstractmethod
    def create(self, resultReportId, content):
        pass
