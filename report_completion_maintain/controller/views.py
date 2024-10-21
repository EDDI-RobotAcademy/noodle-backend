from django.shortcuts import render
from rest_framework import viewsets

from report_completion_maintain.entity.report_completion_maintain import ResultReportCompletionMaintain
from report_completion_maintain.service.report_completion_maintain_service_impl import \
    ResultReportCompletionMaintainServiceImpl


# Create your views here.
class ResultReportCompletionMaintainView(viewsets.ViewSet):
    queryset = ResultReportCompletionMaintain.objects.all()
    resultReportCompletionMaintainService = ResultReportCompletionMaintainServiceImpl.getInstance()

    def create(self, request):
        data = request.data
        resultReportId = data.get("resultReportId")
        score = data.get("score")
        detail = data.get("detail")

        self.resultReportCompletionMaintainService(resultReportId, score, detail)
