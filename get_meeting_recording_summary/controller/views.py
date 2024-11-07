from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from get_meeting_recording_summary.service.get_meeting_recording_summary_service_impl import \
    GetMeetingRecordingSummaryServiceImpl
from github_oauth.service.redis_service_impl import RedisServiceImpl


# Create your views here.
class GetMeetingRecordingSummaryView(viewsets.ViewSet):
    redisService = RedisServiceImpl.getInstance()
    getMeetingRecordingSummaryService = GetMeetingRecordingSummaryServiceImpl.getInstance()

    def getMeetingRecordingSummaryToFastAPI(self, request):
        data = request.data
        userToken = data.get('userToken')['userToken']
        print(f'getMeetingRecordingSummaryToFastAPI() userToken: {userToken}')

        try:
            accountId = self.redisService.getValueByKey(userToken)
            requestComplete = self.getMeetingRecordingSummaryService.getMeetingRecordingSummaryToFastAPI(userToken)

            return Response(requestComplete, status=status.HTTP_200_OK)
        except Exception as e:
            print("getMeetingRecordingSummaryToFastAPI() 중 에러 발생:", e)
            raise e