from abc import abstractmethod, ABC


class MeetingRecordingSummaryRepository(ABC):
    @abstractmethod
    def createSummary(self, username, title, content):
        pass