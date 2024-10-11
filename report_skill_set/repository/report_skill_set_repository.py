from abc import abstractmethod, ABC

class ResultReportSkillSetRepository(ABC):
    @abstractmethod
    def create(self, resultReportId):
        pass