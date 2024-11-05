from subscription.entity.subscription_history import SubscriptionHistory
from subscription.entity.subscription_payment_information import SubscriptionPaymentInformation
from subscription.entity.subscription_type import SubscriptionType
from subscription.entity.subscription_type_selections import SubscriptionTypeSelections
from subscription.repository.subscription_repository import SubscriptionRepository


class SubscriptionRepositoryImpl(SubscriptionRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def registerSubscriptionHistory(self, account):
        return SubscriptionHistory.objects.create(account_id=account)

    def registerSubscriptionTicketType(self, history, type):
        if type == 1:
            return SubscriptionType.objects.create(history_id=history, type=SubscriptionTypeSelections.JUNIOR)
        elif type == 2:
            return SubscriptionType.objects.create(history_id=history, type=SubscriptionTypeSelections.SENIOR)
        elif type == 3:
            return SubscriptionType.objects.create(history_id=history, type=SubscriptionTypeSelections.LEADER)

    def registerSubscriptionPaymentInformation(self, history, paymentID):
        return SubscriptionPaymentInformation.objects.create(history_id=history, paymentID=paymentID)
