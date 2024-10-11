from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from report_title.entity.report_title import ResultReportTitle
from report_title.service.report_title_service_impl import ResultReportTitleServiceImpl


# Create your views here.
class ResultReportTitleView(viewsets.ViewSet):
    queryset = ResultReportTitle.objects.all()
    resultReportTitleService = ResultReportTitleServiceImpl.getInstance()

    def createResultReportTitle(self, request):
        data = request.data
        resultReportId = data.get("resultReportId")
        title = data.get("title")

        self.resultReportTitleService.createResultReportTitle(resultReportId, title)

        return Response({"data": title}, status=status.HTTP_201_CREATED)
