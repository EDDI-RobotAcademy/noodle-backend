from django.shortcuts import render
from rest_framework import viewsets

from report_usage.entity.report_usage import ResultReportUsage
from report_usage.service.report_usage_service_impl import ResultReportUsageServiceImpl


# Create your views here.
class ResultReportUsageView(viewsets.ViewSet):
    queryset = ResultReportUsage.objects.all()
    resultReportUsageService = ResultReportUsageServiceImpl.getInstance()

    def create(self, request):
        data = request.data
        resultReportId = data.get("resultReportId")
        content = data.get("content")

        self.resultReportUsageService.create(resultReportId, content)
