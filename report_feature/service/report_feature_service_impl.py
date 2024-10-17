from report.repository.report_repository_impl import ResultReportRepositoryImpl
from report_feature.repository.report_feature_repository_impl import ResultReportFeatureRepositoryImpl
from report_feature.service.report_feature_service import ResultReportFeatureService


class ResultReportFeatureServiceImpl(ResultReportFeatureService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportFeatureRepository = ResultReportFeatureRepositoryImpl.getInstance()
            cls.__instance.__resultReportRepository = ResultReportRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, resultReportId):
        report = self.__resultReportRepository.getReportById(resultReportId)
        self.__resultReportFeatureRepository.createResultReportFeature(report)
