from abc import ABC, abstractmethod

class BacklogIssueRepository(ABC):
    @abstractmethod
    def create(self, backlog, issue):
        pass