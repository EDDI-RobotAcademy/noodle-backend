from abc import abstractmethod, ABC


class ResultReportOverviewRepository(ABC):
    @abstractmethod
    def createResultReportOverview(self, overview, report):
        pass

    @abstractmethod
    def getResultReportOverviewByResultReport(self, report):
        pass