from abc import abstractmethod, ABC


class ResultReportTeamRepository(ABC):
    @abstractmethod
    def create(self):
        pass