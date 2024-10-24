from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from report_overview.entity.report_overview import ResultReportOverview
from report_overview.service.report_overview_service_impl import ResultReportOverviewServiceImpl


# Create your views here.
class ResultReportOverviewView(viewsets.ViewSet):
    queryset = ResultReportOverview.objects.all()
    resultReportOverviewService = ResultReportOverviewServiceImpl.getInstance()

    def create(self, request):
        data = request.data
        resultReportId = data.get('resultReportId')
        overview = data.get('overview')

        self.resultReportOverviewService.create(resultReportId, overview)

        return Response(status=status.HTTP_201_CREATED)