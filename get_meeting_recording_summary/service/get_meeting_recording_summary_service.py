from abc import abstractmethod, ABC


class GetMeetingRecordingSummaryService(ABC):
    @abstractmethod
    def getMeetingRecordingSummaryToFastAPI(self, userToken):
        pass