from report.repository.report_repository_impl import ResultReportRepositoryImpl
from report_improvement_content.repository.report_improvement_content_repository_impl import \
    ResultReportImprovementContentRepositoryImpl
from report_improvement_content.service.report_improvement_content_service import ResultReportImprovementContentService


class ResultReportImprovementContentServiceImpl(ResultReportImprovementContentService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportImprovementContentRepository = ResultReportImprovementContentRepositoryImpl.getInstance()
            cls.__instance.__resultReportRepository = ResultReportRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, resultReportId, content):
        report = self.__resultReportRepository.getReportById(resultReportId)
        self.__resultReportImprovementContentRepository.createResultReportImprovementContent(report, content)
