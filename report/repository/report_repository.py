from abc import abstractmethod, ABC


class ResultReportRepository(ABC):
    @abstractmethod
    def create(self, creator):
        pass