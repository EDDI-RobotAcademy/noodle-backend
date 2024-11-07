from report.repository.report_repository_impl import ResultReportRepositoryImpl
from report_improvement.repository.report_improvement_repository_impl import ResultReportImprovementRepositoryImpl
from report_improvement.service.report_improvement_service import ResultReportImprovementService


class ResultReportImprovementServiceImpl(ResultReportImprovementService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportImprovementRepository = ResultReportImprovementRepositoryImpl.getInstance()
            cls.__instance.__resultReportRepository = ResultReportRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, resultReportId):
        report = self.__resultReportRepository.getReportById(resultReportId)
        self.__resultReportImprovementRepository.createResultReportImprovement(report)
