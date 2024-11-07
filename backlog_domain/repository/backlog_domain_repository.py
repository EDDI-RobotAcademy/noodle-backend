from abc import ABC, abstractmethod

class BacklogDomainRepository(ABC):
    @abstractmethod
    def create(self, backlog, domain):
        pass

    @abstractmethod
    def modify(self, backlog, domain):
        pass

    @abstractmethod
    def findByBacklog(self, backlog):
        pass