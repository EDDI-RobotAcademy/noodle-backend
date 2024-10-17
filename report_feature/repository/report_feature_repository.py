from abc import abstractmethod, ABC


class ResultReportFeatureRepository(ABC):
    @abstractmethod
    def getResultReportFeatureByResultReport(self, report):
        pass

    @abstractmethod
    def createResultReportFeature(self, report):
        pass