from abc import abstractmethod, ABC


class ResultReportService(ABC):
    @abstractmethod
    def createResultReport(self, creator):
        pass