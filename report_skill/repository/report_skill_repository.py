from abc import abstractmethod, ABC


class ResultReportSkillRepository(ABC):
    @abstractmethod
    def create(self, skill, skillset):
        pass
