from report.repository.report_repository_impl import ResultReportRepositoryImpl
from report_completion.repository.report_completion_repository_impl import ResultReportCompletionRepositoryImpl
from report_completion_maintain.repository.report_completion_maintain_repository_impl import \
    ResultReportCompletionMaintainRepositoryImpl
from report_completion_maintain.service.report_completion_maintain_service import ResultReportCompletionMaintainService


class ResultReportCompletionMaintainServiceImpl(ResultReportCompletionMaintainService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportCompletionMaintainRepository = ResultReportCompletionMaintainRepositoryImpl.getInstance()
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

        self.__resultReportCompletionMaintainRepository.createResultReportCompletionMaintain(completion, score, detail)
