from abc import ABC, abstractmethod

class AccountService(ABC):
    @abstractmethod
    def checkUsernameDuplication(self, username):
        pass

    @abstractmethod
    def findAccountByUsername(self, username):
        pass

    @abstractmethod
    def saveUserNickname(self, nickname):
        pass