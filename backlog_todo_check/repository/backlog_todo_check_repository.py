from abc import ABC, abstractmethod

class BacklogTodoCheckRepository(ABC):
    @abstractmethod
    def create(self, backlog, isChecked):
        pass