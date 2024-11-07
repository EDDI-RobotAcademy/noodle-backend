from django.shortcuts import render
from rest_framework import viewsets

from report_completion_secure.entity.report_completion_secure import ResultReportCompletionSecure
from report_completion_secure.service.report_completion_secure_service_impl import \
    ResultReportCompletionSecureServiceImpl


# Create your views here.
class ResultReportCompletionSecureView(viewsets.ViewSet):
    queryset = ResultReportCompletionSecure.objects.all()
    resultReportCompletionSecureService = ResultReportCompletionSecureServiceImpl.getInstance()

    def create(self, request):
        data = request.data
        resultReportId = data.get("resultReportId")
        score = data.get("score")
        detail = data.get("detail")

        self.resultReportCompletionSecureService.create(resultReportId, score, detail)
