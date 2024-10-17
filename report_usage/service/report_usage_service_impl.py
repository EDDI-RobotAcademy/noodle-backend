from django.db.models.expressions import result

from report.repository.report_repository_impl import ResultReportRepositoryImpl
from report_usage.repository.report_usage_repository_impl import ResultReportUsageRepositoryImpl
from report_usage.service.report_usage_service import ResultReportUsageService


class ResultReportUsageServiceImpl(ResultReportUsageService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportUsageRepository = ResultReportUsageRepositoryImpl.getInstance()
            cls.__instance.__resultReportRepository = ResultReportRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, resultReportId, content):
        report = self.__resultReportRepository.getReportById(resultReportId)
        self.__resultReportUsageRepository.createResultReportUsage(report, content)
