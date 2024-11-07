from subscription.repository.subscription_repository_impl import SubscriptionRepositoryImpl
from subscription.service.subscription_service import SubscriptionService


class SubscriptionServiceImpl(SubscriptionService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__subscriptionRepository = SubscriptionRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def registerSubscriptionHistory(self, account):
        return self.__subscriptionRepository.registerSubscriptionHistory(account)

    def registerSubscriptionTicketType(self, history, type):
        return self.__subscriptionRepository.registerSubscriptionTicketType(history, type)

    def registerSubscriptionPaymentInformation(self, history, paymentID):
        return self.__subscriptionRepository.registerSubscriptionPaymentInformation(history, paymentID)
