from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.service.account_service_impl import AccountServiceImpl
from github_oauth.service.redis_service_impl import RedisServiceImpl
from report_modify.entity.report_modify import ResultReportModify
from report_modify.service.report_modify_service_impl import ResultReportModifyServiceImpl


# Create your views here.
class ResultReportModifyView(viewsets.ViewSet):
    queryset = ResultReportModify.objects.all()
    resultReportModifyService = ResultReportModifyServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()

    def modifyResultReport(self, request):
        data = request.data
        resultReportId = data.get("resultReportId")
        userToken = data.get("userToken")

        if not userToken:
            return Response({"data": "userToken이 존재하지 않습니다!"}, status=status.HTTP_400_BAD_REQUEST)

        accountId = self.redisService.getValueByKey(userToken)
        account = self.accountService.findAccountByAccountId(accountId)
        username = account.username

        self.resultReportModifyService.modifyResultReport(resultReportId, username)

        return Response({"modifier": username}, status=status.HTTP_200_OK)
