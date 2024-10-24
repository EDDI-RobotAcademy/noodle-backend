from abc import abstractmethod, ABC


class ResultReportFeatureContentRepository(ABC):
    @abstractmethod
    def createResultReportFeatureContent(self, resultReportFeatureList, resultReportFeature):
        pass
