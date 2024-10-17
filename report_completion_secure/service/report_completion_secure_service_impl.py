from report.repository.report_repository_impl import ResultReportRepositoryImpl
from report_completion.repository.report_completion_repository_impl import ResultReportCompletionRepositoryImpl
from report_completion_secure.repository.report_completion_secure_repository_impl import \
    ResultReportCompletionSecureRepositoryImpl
from report_completion_secure.service.report_completion_secure_service import ResultReportCompletionSecureService


class ResultReportCompletionSecureServiceImpl(ResultReportCompletionSecureService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportCompletionSecureRepository = ResultReportCompletionSecureRepositoryImpl.getInstance()
            cls.__instance.__resultReportRepository = ResultReportRepositoryImpl.getInstance()
            cls.__instance.__resultReportCompletionRepository = ResultReportCompletionRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, resultReportId, score, detail):
        report = self.__resultReportRepository.getReportById(resultReportId)
        completion = self.__resultReportCompletionRepository.getResultRepositoryCompletionByResultReport(report)
        self.__resultReportCompletionSecureRepository.createResultReportCompletionSecure(completion, score, detail)

