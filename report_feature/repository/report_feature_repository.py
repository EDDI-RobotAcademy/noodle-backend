from abc import abstractmethod, ABC


class ResultReportFeatureRepository(ABC):
    @abstractmethod
    def createResultReportFeature(self, report):
        pass