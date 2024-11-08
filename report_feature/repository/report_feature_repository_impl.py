from report_feature.entity.report_feature import ResultReportFeature
from report_feature.repository.report_feature_repository import ResultReportFeatureRepository


class ResultReportFeatureRepositoryImpl(ResultReportFeatureRepository):
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

    def getResultReportFeatureByResultReport(self, report):
        return ResultReportFeature.objects.get(report=report)

    def createResultReportFeature(self, report):
        return ResultReportFeature.objects.create(report=report)

    def delete(self, report):
        ResultReportFeature.objects.get(report=report).delete()
