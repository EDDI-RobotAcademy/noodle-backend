from get_result_report.repository.get_result_report_repository_impl import GetResultReportRepositoryImpl
from get_result_report.service.get_result_report_service import GetResultReportService


class GetResultReportServiceImpl(GetResultReportService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__getResultReportRepository = GetResultReportRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getResultReportToFastAPI(self, userToken):
        try:
            resultReport = self.__getResultReportRepository.getResultReport(userToken)
            return resultReport
        except Exception as e:
            print("getResultReportToFastAPI 중 에러 발생!:", e)
            raise e

