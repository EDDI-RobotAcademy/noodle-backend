from abc import ABC, abstractmethod


class SubscriptionRepository(ABC):
    @abstractmethod
    def registerSubscriptionHistory(self, account):
        pass

    @abstractmethod
    def registerSubscriptionTicketType(self, history, type):
        pass

    @abstractmethod
    def registerSubscriptionPaymentInformation(self, history, paymentID):
        pass
