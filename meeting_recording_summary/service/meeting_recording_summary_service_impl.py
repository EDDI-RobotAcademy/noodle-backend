from account.repository.account_repostiory_impl import AccountRepositoryImpl
from meeting_recording_summary.repository.meeting_recording_summary_repository_impl import \
    MeetingRecordingSummaryRepositoryImpl
from meeting_recording_summary.service.meeting_recording_summary_service import MeetingRecordingSummaryService


class MeetingRecordingSummaryServiceImpl(MeetingRecordingSummaryService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__meetingRecordingSummaryRepository = MeetingRecordingSummaryRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, accountId, title, content):
        account = self.__accountRepository.findAccountByAccountId(accountId)
        meetingRecordingSummary = self.__meetingRecordingSummaryRepository.createSummary(account.username, title, content)

        return meetingRecordingSummary

    def list(self, offset, limit):
        summaryList = self.__meetingRecordingSummaryRepository.getPagedSummaryList(offset, limit)
        meetingRecordingSummaryList = []

        for summary in summaryList:
            meetingRecordingSummaryList.append({
                'id': summary.id,
                'title': summary.title,
                'writer': summary.writer,
                'content': summary.content,
                'regData': summary.regDate
            })

        return meetingRecordingSummaryList

    def read(self, meetingRecordingSummaryId):
        summary = (
            self.__meetingRecordingSummaryRepository.getMeetingRecordingSummaryByMeetingRecordingSummaryId(meetingRecordingSummaryId))

        meetingRecordingSummary = {
            "id": summary.id,
            "title": summary.title,
            "writer": summary.writer,
            "content": summary.content,
            "regDate": summary.regDate
        }

        return meetingRecordingSummary


