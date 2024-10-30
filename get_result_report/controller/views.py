from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from get_result_report.service.get_result_report_service_impl import GetResultReportServiceImpl
from github_oauth.service.redis_service_impl import RedisServiceImpl


# Create your views here.
class GetResultReportView(viewsets.ViewSet):
    redisService = RedisServiceImpl.getInstance()
    getResultReportService = GetResultReportServiceImpl.getInstance()

    def getResultReportToFastAPI(self, request):
        data = request.data
        userToken = data.get('userToken')

        try:
            accountId = self.redisService.getValueByKey(userToken)
            requestComplete = self.getResultReportService.getResultReportToFastAPI(userToken)

            return Response(requestComplete, status=status.HTTP_200_OK)
        except Exception as e:
            print("aiRequestToFastAPI() 중 에러 발생:", e)
            raise e

