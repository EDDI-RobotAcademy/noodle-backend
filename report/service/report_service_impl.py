from report.repository.report_repository_impl import ResultReportRepositoryImpl
from report.service.report_service import ResultReportService


class ResultReportServiceImpl(ResultReportService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportRepository = ResultReportRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createResultReport(self, creator):
        return self.__resultReportRepository.create(creator)

