from abc import abstractmethod, ABC


class ResultReportRepository(ABC):
    @abstractmethod
    def getReportById(self, id):
        pass

    @abstractmethod
    def create(self, creator):
        pass

    @abstractmethod
    def getAllResultReportList(self):
        pass