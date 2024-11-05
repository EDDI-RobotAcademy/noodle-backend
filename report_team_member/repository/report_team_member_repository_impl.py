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
        resultReportTeamMemberList = [ResultReportTeamMember(
            name=member['name'], role=member['role'], department=member['department'], team=resultReportTeam) for member
            in teamMember]

        ResultReportTeamMember.objects.bulk_create(resultReportTeamMemberList)
        return resultReportTeamMemberList

    def getResultReportTeamMemberListByResultReportTeam(self, resultReportTeam):
        resultReportTeamMembers = ResultReportTeamMember.objects.filter(team=resultReportTeam)
        resultReportTeamMemberList = [[member.name, member.role, member.department] for member in
                                      resultReportTeamMembers]

        return resultReportTeamMemberList

    def getResultReportTeamMemberByResultReportTeamAndName(self, resultReportTeam, name):
        try:
            return ResultReportTeamMember.objects.get(name=name, team=resultReportTeam)
        except ResultReportTeamMember.DoesNotExist:
            return None

    def modify(self, teamObj, modifiedMemberList):
        ResultReportTeamMember.objects.filter(team=teamObj).delete()

        resultReportTeamMemberList = [ResultReportTeamMember(
            name=member['name'], role=member['role'], department=member['department'], team=teamObj) for member
            in modifiedMemberList]

        ResultReportTeamMember.objects.bulk_create(resultReportTeamMemberList)

    def delete(self, teamObj):
        ResultReportTeamMember.objects.filter(team=teamObj).delete()
