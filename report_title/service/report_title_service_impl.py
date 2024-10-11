from report_title.repository.report_title_repository_impl import ResultReportTitleRepositoryImpl
from report_title.service.report_title_service import ResultReportTitleService


class ResultReportTitleServiceImpl(ResultReportTitleService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportTitleRepository = ResultReportTitleRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createResultReportTitle(self, resultReportId, title):
        self.__resultReportTitleRepository.create(resultReportId, title)
