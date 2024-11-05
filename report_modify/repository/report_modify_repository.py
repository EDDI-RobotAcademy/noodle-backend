from abc import abstractmethod, ABC


class ResultReportModifyRepository(ABC):
    @abstractmethod
    def create(self, report, modifier):
        pass

    @abstractmethod
    def getModifierByResultReport(self, report):
        pass

    @abstractmethod
    def delete(self, report):
        pass
