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

    def createResultReportTeamMember(self, teamMember, resultReportTeam):
        resultReportTeamMemberList = [ResultReportTeamMember(name=member[0], role=member[1], team=resultReportTeam)
                                      for member in teamMember]

        ResultReportTeamMember.objects.bulk_create(resultReportTeamMemberList)
        return resultReportTeamMemberList

    def getResultReportTeamMemberListByResultReportTeam(self, resultReportTeam):
        resultReportTeamMembers = ResultReportTeamMember.objects.filter(team=resultReportTeam)
        resultReportTeamMemberList = [[member.name, member.role, member.department] for member in resultReportTeamMembers]

        return resultReportTeamMemberList
