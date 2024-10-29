from abc import abstractmethod, ABC


class AIRequestRepository(ABC):
    @abstractmethod
    def aiRequest(self, userToken, username, command, data):
        pass