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
        title = data.get("title")
        overview = data.get("overview")
        teamMemberList = data.get("teamMemberList")
        skillList = data.get("skillList")
        featureList = data.get("featureList")
        usage = data.get("usage")
        improvementList = data.get("improvementList")
        completionList = data.get('completionList')

        if not userToken:
            return Response({"data": "userToken이 존재하지 않습니다!"}, status=status.HTTP_400_BAD_REQUEST)

        accountId = self.redisService.getValueByKey(userToken)
        account = self.accountService.findAccountByAccountId(accountId)
        username = account.username

        createdResultReportId = self.resultReportService.createResultReport(
            username, title, overview, teamMemberList, skillList, featureList, usage, improvementList,
            completionList).id

        return Response({"data": createdResultReportId}, status=status.HTTP_201_CREATED)

    def list(self, request):
        data = request.data
        query = data.get('query', '').strip()
        page = int(data.get('page', 1))
        perPage = int(data.get('perPage', 10))

        print('query:', query)
        print('page:', page)
        print('perPage:', perPage)

        offset = (page - 1) * perPage
        limit = offset + perPage

        resultReportList = self.resultReportService.list(query=query)
        totalCount = len(resultReportList)

        return Response({"resultReports": resultReportList[offset:limit], "totalCount": totalCount},
                        status=status.HTTP_200_OK)

    def read(self, request):
        data = request.data
        resultReportId = data.get('resultReportId')

        resultReport = self.resultReportService.read(resultReportId)

        return Response(resultReport, status=status.HTTP_200_OK)

    def modify(self, request):
        try:
            data = request.data
            resultReportId = data.get('id')

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)
            account = self.accountService.findAccountByAccountId(accountId)
            username = account.username

            modifiedReport = data.get('modifiedReport')
            print(modifiedReport)

            bool = self.resultReportService.modify(resultReportId, username, modifiedReport)
            if bool == True:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            data = request.data
            resultReportId = data.get('resultReportId')

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)
            account = self.accountService.findAccountByAccountId(accountId)
            username = account.username

            bool = self.resultReportService.delete(resultReportId, username)
            if bool == True:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def validation(self, request):
        try:
            data = request.data
            id = data.get('id')
            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)
            account = self.accountService.findAccountByAccountId(accountId)
            username = account.username

            bool = self.resultReportService.validateUser(id, username)

            if bool == True:
                return Response(True, status=status.HTTP_200_OK)
            else:
                return Response(False, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
