from abc import abstractmethod, ABC


class ResultReportFeatureContentRepository(ABC):
    @abstractmethod
    def createResultReportFeatureContent(self, resultReportFeatureList, resultReportFeature):
        pass

    @abstractmethod
    def getResultReportFeatureListByResultReportFeature(self, feature):
        pass

    @abstractmethod
    def modify(self, featureObj, featureList):
        pass

    @abstractmethod
    def delete(self, featureObj):
        pass
