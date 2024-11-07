from abc import ABC, abstractmethod


class BacklogService(ABC):
    @abstractmethod
    def createBacklog(self, backlogList):
        pass

    @abstractmethod
    def getBacklogs(self, startIdx, endIdx):
        pass
