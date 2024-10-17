from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from report_improvement.entity.report_improvement import ResultReportImprovement
from report_improvement.service.report_improvement_service_impl import ResultReportImprovementServiceImpl


# Create your views here.
class ResultReportImprovementView(viewsets.ViewSet):
    queryset = ResultReportImprovement.objects.all()
    resultReportImprovementService = ResultReportImprovementServiceImpl.getInstance()

    def create(self, request):
        data = request.data
        resultReportId = data.get("resultReportId")

        self.resultReportImprovementService.create(resultReportId)

        return Response(status=status.HTTP_201_CREATED)
