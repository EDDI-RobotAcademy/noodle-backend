from abc import ABC, abstractmethod

class BacklogReviewRepository(ABC):
    @abstractmethod
    def create(self, backlog, review):
        pass