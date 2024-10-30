from abc import ABC, abstractmethod


class BacklogSuccessCriteriaRepository(ABC):
    @abstractmethod
    def create(self, backlog, successCriteria):
        pass

    @abstractmethod
    def findByBacklog(self, backlog):
        pass
