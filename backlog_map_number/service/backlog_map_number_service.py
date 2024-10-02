from abc import ABC, abstractmethod

class BacklogMapNumberService(ABC):
    @abstractmethod
    def createBacklogMapNumber(self, backlogId, backlogMapNumber):
        pass