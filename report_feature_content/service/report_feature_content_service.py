from abc import abstractmethod, ABC


class ResultReportFeatureContentService(ABC):
    @abstractmethod
    def create(self, resultReportId):
        pass
