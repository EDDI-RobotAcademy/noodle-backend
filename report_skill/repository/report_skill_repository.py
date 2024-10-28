from abc import abstractmethod, ABC


class ResultReportSkillRepository(ABC):
    @abstractmethod
    def create(self, skillList, skillset):
        pass

    @abstractmethod
    def getResultReportSkillListByResultReportSkillSet(self, skillSet):
        pass