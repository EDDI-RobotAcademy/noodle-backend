from abc import abstractmethod, ABC


class ResultReportTitleService(ABC):
    @abstractmethod
    def createResultReportTitle(self, resultReportId, title):
        pass