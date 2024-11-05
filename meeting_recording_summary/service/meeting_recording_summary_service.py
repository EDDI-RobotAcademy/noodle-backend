from abc import abstractmethod, ABC


class MeetingRecordingSummaryService(ABC):
    @abstractmethod
    def create(self, accountId, title, content):
        pass
