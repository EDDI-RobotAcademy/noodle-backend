from report_team_member.entity.report_team_member import ResultReportTeamMember
from report_team_member.repository.report_team_member_repository import ResultReportTeamMemberRepository


class ResultReportTeamMemberRepositoryImpl(ResultReportTeamMemberRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createResultReportTeamMember(self, name, role, resultReportTeamId):
        ResultReportTeamMember.objects.create(name=name, role=role, team_id=resultReportTeamId)
