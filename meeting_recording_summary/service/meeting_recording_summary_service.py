from abc import abstractmethod, ABC


class MeetingRecordingSummaryService(ABC):
    @abstractmethod
    def create(self, accountId, title, content):
        pass

    @abstractmethod
    def list(self, offset, limit):
        pass

    @abstractmethod
    def read(self, meetingRecordingSummaryId):
        pass