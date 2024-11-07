from django.shortcuts import render
from rest_framework import viewsets

from report_completion_total.entity.report_completion_total import ResultReportCompletionTotal
from report_completion_total.service.report_completion_total_service_impl import ResultReportCompletionTotalServiceImpl


# Create your views here.
class ResultReportCompletionTotalView(viewsets.ViewSet):
    queryset = ResultReportCompletionTotal.objects.all()
    resultReportCompletionTotalService = ResultReportCompletionTotalServiceImpl.getInstance()

    def create(self, request):
        data = request.data
        resultReportId = data.get("resultReportId")
        score = data.get("score")
        detail = data.get("detail")

        self.resultReportCompletionTotalService.create(resultReportId, score, detail)
