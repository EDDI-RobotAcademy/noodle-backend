from abc import abstractmethod, ABC


class ResultReportSkillSetRepository(ABC):
    @abstractmethod
    def getResultReportSkillSetByResultReport(self, report):
        pass

    @abstractmethod
    def create(self, report):
        pass

    @abstractmethod
    def delete(self, report):
        pass
