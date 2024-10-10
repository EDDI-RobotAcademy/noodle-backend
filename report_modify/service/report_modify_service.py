from abc import abstractmethod, ABC


class ResultReportModifyService(ABC):
    @abstractmethod
    def createResultReportModify(self, resultReportId, username):
        pass