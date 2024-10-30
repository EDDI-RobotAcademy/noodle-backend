from abc import abstractmethod, ABC


class GetResultReportRepository(ABC):
    @abstractmethod
    def getResultReport(self, userToken):
        pass