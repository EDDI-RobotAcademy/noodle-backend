from abc import abstractmethod, ABC


class ResultReportFeatureService(ABC):
    @abstractmethod
    def create(self, resultReportId):
        pass
