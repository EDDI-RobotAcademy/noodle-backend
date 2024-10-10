from abc import abstractmethod, ABC

class ResultReportModifyRepository(ABC):
    @abstractmethod
    def modify(self, resultReportId, modifier):
        pass