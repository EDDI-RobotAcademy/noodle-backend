from api.http_request import HttpRequestInstance
from get_meeting_recording_summary.repository.get_meeting_recording_summary_repository import GetMeetingRecordingSummaryRepository


class GetMeetingRecordingSummaryRepositoryImpl(GetMeetingRecordingSummaryRepository):
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

    def getMeetingRecordingSummary(self, userToken):
        endpoint = "/meeting-recording-summary-result"

        payload = {
            "userToken": userToken,
        }

        print(f"userToken: {userToken}")

        response = HttpRequestInstance.post(endpoint, data=payload)

        if response:
            print("AI Request Success:", response)
            return response
        else:
            print("AI Request Failed")
            return None
