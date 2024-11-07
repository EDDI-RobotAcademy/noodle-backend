from get_meeting_recording_summary.repository.get_meeting_recording_summary_repository_impl import \
    GetMeetingRecordingSummaryRepositoryImpl
from get_meeting_recording_summary.service.get_meeting_recording_summary_service import GetMeetingRecordingSummaryService


class GetMeetingRecordingSummaryServiceImpl(GetMeetingRecordingSummaryService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__getMeetingRecordingSummaryRepository = GetMeetingRecordingSummaryRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getMeetingRecordingSummaryToFastAPI(self, userToken):
        try:
            meetingRecordingSummary = self.__getMeetingRecordingSummaryRepository.getMeetingRecordingSummary(userToken)
            return meetingRecordingSummary
        except Exception as e:
            print("getMeetingRecordingSummaryToFastAPI 중 에러 발생!:", e)
            raise e