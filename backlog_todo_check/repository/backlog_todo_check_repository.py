from abc import ABC, abstractmethod

class BacklogTodoCheckRepository(ABC):
    @abstractmethod
    def create(self, todo, isChecked):
        pass