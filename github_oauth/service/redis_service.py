from abc import ABC, abstractmethod


class RedisService(ABC):
    @abstractmethod
    def store_access_token(self, account_id, access_token):
        pass

    @abstractmethod
    def getValueByKey(self, key):
        pass

    @abstractmethod
    def setBacklogCreationFlag(self, userToken, flag):
        pass

    @abstractmethod
    def getBacklogCreationFlag(self, userToken):
        pass

    @abstractmethod
    def setSubscriptionRemainingTime(self, userToken, ticketType):
        pass

    @abstractmethod
    def checkSubscription(self, userToken):
        pass
