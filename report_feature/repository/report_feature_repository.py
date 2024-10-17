from abc import abstractmethod, ABC


class ResultReportFeatureRepository(ABC):
    @abstractmethod
    def getResultReportFeatureById(self, id):
        pass

    @abstractmethod
    def createResultReportFeature(self, report):
        pass