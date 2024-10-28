from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.service.account_service_impl import AccountServiceImpl
from github_oauth.service.redis_service_impl import RedisServiceImpl
from report.entity.report import ResultReport
from report.service.report_service_impl import ResultReportServiceImpl


# Create your views here.
class ResultReportView(viewsets.ViewSet):
    queryset = ResultReport.objects.all()
    resultReportService = ResultReportServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()

    def createResultReport(self, request):
        data = request.data
        userToken = data.get("userToken")
        message = data.get("message")

        if not userToken:
            return Response({"data": "userToken이 존재하지 않습니다!"}, status=status.HTTP_400_BAD_REQUEST)

        accountId = self.redisService.getValueByKey(userToken)
        account = self.accountService.findAccountByAccountId(accountId)
        username = account.username

        createdResultReportId = self.resultReportService.createResultReport(username, **message).id

        return Response({"data": createdResultReportId}, status=status.HTTP_201_CREATED)

    def list(self, request):
        resultReportList = self.resultReportService.list()

        return Response({"data": resultReportList}, status=status.HTTP_200_OK)

    def read(self, request):
        data = request.data
        resultReportId = data.get('resultReportId')

        resultReport = self.resultReportService.read(resultReportId)

        return Response(resultReport, status=status.HTTP_200_OK)
