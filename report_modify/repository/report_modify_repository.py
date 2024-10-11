from abc import abstractmethod, ABC

class ResultReportModifyRepository(ABC):
    @abstractmethod
    def create(self, resultReportId, modifier):
        pass