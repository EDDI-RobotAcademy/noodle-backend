from report.repository.report_repository_impl import ResultReportRepositoryImpl
from report_overview.repository.report_overview_repository_impl import ResultReportOverviewRepositoryImpl
from report_overview.service.report_overview_service import ResultReportOverviewService


class ResultReportOverviewServiceImpl(ResultReportOverviewService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportOverviewRepository = ResultReportOverviewRepositoryImpl.getInstance()
            cls.__instance.__resultReportRepository = ResultReportRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, resultReportId, overview):
        report = self.__resultReportRepository.getReportById(resultReportId)
        resultReportOverview = self.__resultReportOverviewRepository.createResultReportOverview(overview, report)

        return resultReportOverview

