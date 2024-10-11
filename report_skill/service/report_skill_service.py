from abc import abstractmethod, ABC


class ResultReportSkillService(ABC):
    @abstractmethod
    def createResultReportSkill(self, skill, skillSetId):
        pass
