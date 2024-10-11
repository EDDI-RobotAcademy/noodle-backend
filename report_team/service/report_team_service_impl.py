from report_team.repository.result_team_repository_impl import ResultReportTeamRepositoryImpl
from report_team.service.report_team_service import ResultReportTeamService


class ResultReportTeamServiceImpl(ResultReportTeamService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportTeamRepository = ResultReportTeamRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createResultReportTeamService(self):
        self.__resultReportTeamRepository.create()
