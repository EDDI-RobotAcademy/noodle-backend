from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from report_completion.entity.report_completion import ResultReportCompletion
from report_completion.service.report_completion_service_impl import ResultReportCompletionServiceImpl


# Create your views here.
class ResultReportCompletionView(viewsets.ViewSet):
    queryset = ResultReportCompletion.objects.all()
    resultReportCompletionService = ResultReportCompletionServiceImpl.getInstance()

    def create(self, request):
        data = request.data
        resultReportId = data.get("resultReportId")

        self.resultReportCompletionService.create(resultReportId)

        return Response(status=status.HTTP_201_CREATED)
