from abc import abstractmethod, ABC


class ResultReportOverviewService(ABC):
    @abstractmethod
    def create(self, resultReportId, overview):
        pass
