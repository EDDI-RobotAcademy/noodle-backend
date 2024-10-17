from report.repository.report_repository_impl import ResultReportRepositoryImpl
from report_modify.repository.report_modify_repository_impl import ResultReportModifyRepositoryImpl
from report_modify.service.report_modify_service import ResultReportModifyService


class ResultReportModifyServiceImpl(ResultReportModifyService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportModifyRepository = ResultReportModifyRepositoryImpl.getInstance()
            cls.__instance.__resultReportRepository = ResultReportRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createResultReportModify(self, resultReportId, username):
        report = self.__resultReportRepository.getReportById(resultReportId)
        self.__resultReportModifyRepository.create(report, username)
