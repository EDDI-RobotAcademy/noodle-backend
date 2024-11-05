from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from github_oauth.service.redis_service_impl import RedisServiceImpl
from meeting_recording_summary.entity.meeting_recording_summary import MeetingRecordingSummary
from meeting_recording_summary.service.meeting_recording_summary_service_impl import MeetingRecordingSummaryServiceImpl


# Create your views here.
class MeetingRecordingSummaryView(viewsets.ViewSet):
    queryset = MeetingRecordingSummary.objects.all()
    meetingRecordingSummaryService = MeetingRecordingSummaryServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def create(self, request):
        data = request.data
        userToken = data.get('userToken')
        title = data.get('title')
        content = data.get('content')

        try:
            accountId = self.redisService.getValueByKey(userToken)
        except Exception as e:
            print("회의록 저장 중 에러 발생:", e)
            raise e

        meetingRecordingSummary = self.meetingRecordingSummaryService.create(accountId, title, content)

        return Response(data={'meetingRecordingSummaryId': meetingRecordingSummary.id}, status=status.HTTP_201_CREATED)

    def list(self, request):
        data = request.data
        userToken = data.get('userToken')
        page = data.get('page', 1)
        perPage = data.get('perPage', 10)

        try:
            accountId = self.redisService.getValueByKey(userToken)
        except Exception as e:
            print("회의록 리스트 불러오는 중 에러 발생:", e)
            raise e

        offset = (page - 1) * perPage
        limit = offset + perPage

        meetingRecordingSummaryList = self.meetingRecordingSummaryService.list(offset, limit)

        return Response(data={'meetingRecordingSummaryList': meetingRecordingSummaryList}, status=status.HTTP_200_OK)

    def read(self, request):
        data = request.data
        userToken = data.get("userToken")
        meetingRecordingSummaryId = data.get("meetingRecordingSummaryId")

        try:
            accountId = self.redisService.getValueByKey(userToken)
        except Exception as e:
            print("회의록 읽는 중 에러 발생:", e)
            raise e

        meetingRecordingSummary = self.meetingRecordingSummaryService.read(meetingRecordingSummaryId)

        return Response(data={'meetingRecordingSummary': meetingRecordingSummary}, status=status.HTTP_200_OK)