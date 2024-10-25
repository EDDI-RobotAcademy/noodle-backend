from abc import ABC, abstractmethod

class BacklogRepository(ABC):
    @abstractmethod
    def create(self, title):
        pass

    @abstractmethod
    def findById(self, backlogId):
        pass

    @abstractmethod
    def getTotalNumberOfBacklog(self):
        pass