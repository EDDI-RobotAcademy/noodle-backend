from abc import abstractmethod, ABC


class ResultReportSkillSetService(ABC):
    @abstractmethod
    def createResultReportSkillSet(self, resultReportId):
        pass