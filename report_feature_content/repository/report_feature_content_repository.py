from abc import abstractmethod, ABC


class ResultReportFeatureContentRepository(ABC):
    @abstractmethod
    def createResultReportFeatureContent(self, resultReportFeatureList, resultReportFeature):
        pass

    @abstractmethod
    def getResultReportFeatureListByResultReportFeature(self, feature):
        pass