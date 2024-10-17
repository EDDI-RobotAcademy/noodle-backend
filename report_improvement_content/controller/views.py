from django.shortcuts import render
from rest_framework import viewsets

from report_improvement_content.entity.report_improvement_content import ResultReportImprovementContent
from report_improvement_content.service.report_improvement_content_service_impl import \
    ResultReportImprovementContentServiceImpl


# Create your views here.
class ResultReportImprovementContentView(viewsets.ViewSet):
    queryset = ResultReportImprovementContent.objects.all()
    resultReportImprovementContentService = ResultReportImprovementContentServiceImpl.getInstance()

    def create(self, request):
        data = request.data
        resultReportId = data.get("resultReportId")
        content = data.get("content")

        self.resultReportImprovementContentService.create(resultReportId, content)
