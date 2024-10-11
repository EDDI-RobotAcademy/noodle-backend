from abc import abstractmethod, ABC


class ResultReportTitleRepository(ABC):
    @abstractmethod
    def create(self, resultReportId, title):
        pass
