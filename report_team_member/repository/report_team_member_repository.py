from abc import abstractmethod, ABC


class ResultReportTeamMemberRepository(ABC):
    @abstractmethod
    def createResultReportTeamMember(self, name, role, resultReportTeam):
        pass