from abc import abstractmethod, ABC


class ResultReportUsageRepository(ABC):
    @abstractmethod
    def createResultReportUsage(self, report, content):
        pass

    @abstractmethod
    def getResultReportUsageByResultReport(self, report):
        pass

    @abstractmethod
    def modify(self, usageObj, usages):
        pass

    @abstractmethod
    def delete(self, report):
        pass
