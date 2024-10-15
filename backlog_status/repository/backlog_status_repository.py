from abc import ABC, abstractmethod

class BacklogStatusRepository(ABC):
    @abstractmethod
    def create(self, backlog, backlogStatus):
        pass