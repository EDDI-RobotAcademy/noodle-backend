from abc import ABC, abstractmethod

class BacklogSuccessCriteriaRepository(ABC):
    @abstractmethod
    def create(self, backlog, successCriteria):
        pass