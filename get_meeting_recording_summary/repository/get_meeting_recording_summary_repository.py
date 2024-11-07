from abc import abstractmethod, ABC


class GetMeetingRecordingSummaryRepository(ABC):
    @abstractmethod
    def getMeetingRecordingSummary(self, userToken):
        pass