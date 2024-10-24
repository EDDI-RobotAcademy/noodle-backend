from abc import abstractmethod, ABC


class ResultReportService(ABC):
    @abstractmethod
    def createResultReport(self, username, **kwargs):
        pass