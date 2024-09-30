from abc import ABC, abstractmethod

class BacklogDomainRepository(ABC):
    @abstractmethod
    def create(self, backlog, domain):
        pass