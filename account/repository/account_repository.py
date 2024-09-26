from abc import ABC, abstractmethod

class AccountRepository(ABC):
    @abstractmethod
    def findAccountByUsername(self, username):
        pass

    @abstractmethod
    def findAccountByAccountId(self, account_id):
        pass

    @abstractmethod
    def saveAccountByUsername(self, nickname):
        pass