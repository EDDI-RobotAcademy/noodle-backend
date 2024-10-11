from abc import abstractmethod, ABC

class ResultReportTeamMemberService(ABC):
    @abstractmethod
    def createResultReportTeamMember(self, name, role, resultReportTeamId):
        pass