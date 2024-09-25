from abc import ABC, abstractmethod

class AccountService(ABC):
    @abstractmethod
    def checkUsernameDuplication(self, username):
        pass