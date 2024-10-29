from abc import abstractmethod, ABC


class AIRequestService(ABC):
    @abstractmethod
    def aiRequestToFastAPI(self, userToken, accountId, command, data):
        pass