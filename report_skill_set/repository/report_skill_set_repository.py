from abc import abstractmethod, ABC

class ResultReportSkillSetRepository(ABC):
    @abstractmethod
    def getResultReportSkillSetById(self, id):
        pass

    @abstractmethod
    def create(self, report):
        pass