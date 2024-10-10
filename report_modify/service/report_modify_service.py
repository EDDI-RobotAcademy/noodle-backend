from abc import abstractmethod, ABC


class ResultReportModifyService(ABC):
    @abstractmethod
    def modifyResultReport(self, resultReportId, username):
        pass