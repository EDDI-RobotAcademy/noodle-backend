from abc import ABC, abstractmethod

class BacklogSuccessCriteriaService(ABC):
    @abstractmethod
    def createBacklogSuccessCriteria(self, backlogId, successCriteria):
        pass