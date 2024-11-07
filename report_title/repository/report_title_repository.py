from abc import abstractmethod, ABC


class ResultReportTitleRepository(ABC):
    @abstractmethod
    def create(self, report, title):
        pass

    @abstractmethod
    def getAllResultReportTitleList(self):
        pass

    @abstractmethod
    def getResultReportTitleByResultReport(self, report):
        pass

    @abstractmethod
    def getSearchResultReportTitle(self, query):
        pass

    @abstractmethod
    def modify(self, obj, title):
        pass

    @abstractmethod
    def delete(self, obj):
        pass