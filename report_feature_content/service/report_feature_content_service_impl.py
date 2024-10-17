from report.repository.report_repository_impl import ResultReportRepositoryImpl
from report_feature.repository.report_feature_repository_impl import ResultReportFeatureRepositoryImpl
from report_feature_content.service.report_feature_content_service import ResultReportFeatureContentService


class ResultReportFeatureContentServiceImpl(ResultReportFeatureContentService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportFeatureContentRepository = ResultReportFeatureContentRepositoryImpl.getInstance()
            cls.__instance.__resultReportRepository = ResultReportRepositoryImpl.getInstance()
            cls.__instance.__resultReportFeatureRepository = ResultReportFeatureRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, resultReportId):
        report = self.__resultReportRepository.getReportById(resultReportId)
        resultReportFeature = self.__resultReportFeatureRepository.getResultReportFeatureByResultReport(report)
        self.__resultReportFeatureContentRepository.createResultReportFeatureContent(resultReportFeature)

