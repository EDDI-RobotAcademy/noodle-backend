from abc import abstractmethod, ABC


class GetResultReportService(ABC):
    @abstractmethod
    def getResultReportToFastAPI(self, userToken):
        pass