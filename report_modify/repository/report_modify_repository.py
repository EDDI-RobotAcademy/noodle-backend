from abc import abstractmethod, ABC

class ResultReportModifyRepository(ABC):
    @abstractmethod
    def create(self, report, modifier):
        pass