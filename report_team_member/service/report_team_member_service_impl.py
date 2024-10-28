from report.repository.report_repository_impl import ResultReportRepositoryImpl
from report_team.repository.result_team_repository_impl import ResultReportTeamRepositoryImpl
from report_team_member.repository.report_team_member_repository_impl import ResultReportTeamMemberRepositoryImpl
from report_team_member.service.report_team_member_service import ResultReportTeamMemberService


class ResultReportTeamMemberServiceImpl(ResultReportTeamMemberService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportTeamMemberRepository = ResultReportTeamMemberRepositoryImpl.getInstance()
            cls.__instance.__resultReportTeamRepository = ResultReportTeamRepositoryImpl.getInstance()
            cls.__instance.__resultReportRepository = ResultReportRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createResultReportTeamMember(self, name, role, resultReportId):
        resultReport = self.__resultReportRepository.getReportById(resultReportId)
        resultReportTeam = self.__resultReportTeamRepository.getResultReportTeamByResultReport(resultReport)
        self.__resultReportTeamMemberRepository.create(name, role, resultReportTeam)
