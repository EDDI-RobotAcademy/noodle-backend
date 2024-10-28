from abc import abstractmethod, ABC


class ResultReportUsageRepository(ABC):
    @abstractmethod
    def createResultReportUsage(self, report, content):
        pass

    @abstractmethod
    def getResultReportUsageByResultReport(self, report):
        pass