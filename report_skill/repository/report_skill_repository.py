from abc import abstractmethod, ABC


class ResultReportSkillRepository(ABC):
    @abstractmethod
    def create(self, skillList, skillset):
        pass
