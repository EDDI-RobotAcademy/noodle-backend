from report.repository.report_repository_impl import ResultReportRepositoryImpl
from report_completion.repository.report_completion_repository_impl import ResultReportCompletionRepositoryImpl
from report_completion.service.report_completion_service import ResultReportCompletionService


class ResultReportCompletionServiceImpl(ResultReportCompletionService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportCompletionRepository = ResultReportCompletionRepositoryImpl.getInstance()
            cls.__instance.__resultReportRepository = ResultReportRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, resultReportId):
        report = self.__resultReportRepository.getReportById(resultReportId)
        self.__resultReportCompletionRepository.createResultReportCompletion(report)
