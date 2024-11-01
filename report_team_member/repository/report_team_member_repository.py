from abc import abstractmethod, ABC


class ResultReportTeamMemberRepository(ABC):
    @abstractmethod
    def createResultReportTeamMember(self, teamMember, resultReportTeam):
        pass

    @abstractmethod
    def getResultReportTeamMemberListByResultReportTeam(self, resultReportTeam):
        pass

    @abstractmethod
    def getResultReportTeamMemberByResultReportTeamAndName(self, resultReportTeam, name):
        pass