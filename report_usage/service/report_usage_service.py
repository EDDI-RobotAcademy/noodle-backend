from abc import abstractmethod, ABC


class ResultReportUsageService(ABC):
    @abstractmethod
    def create(self, resultReportId, content):
        pass