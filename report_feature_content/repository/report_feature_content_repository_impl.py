from report_feature_content.entity.report_feature_content import ResultReportFeatureContent
from report_feature_content.repository.report_feature_content_repository import ResultReportFeatureContentRepository


class ResultReportFeatureContentRepositoryImpl(ResultReportFeatureContentRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createResultReportFeatureContent(self, reportContentList, resultReportFeature):
        resultReportFeatureContentList = [ResultReportFeatureContent(content=content, feature=resultReportFeature)
                                          for content in reportContentList]
        ResultReportFeatureContent.objects.bulk_create(resultReportFeatureContentList)

        return resultReportFeatureContentList
    