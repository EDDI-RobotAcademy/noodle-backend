from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from report.entity.report import ResultReport
from report.service.report_service_impl import ResultReportServiceImpl


# Create your views here.
class ResultReportView(viewsets.ViewSet):
    queryset = ResultReport.objects.all()
    resultReportService = ResultReportServiceImpl.getInstance()

    def createResultReport(self, request):
        data = request.data
        creator = data.get('creator')

        if not creator:
            return Response({"data": "생성자는 반드시 포함되어야 합니다."}, status=status.HTTP_400_BAD_REQUEST)

        createdResultReportId = self.resultReportService.createResultReport(creator).id

        return Response({"data": createdResultReportId}, status=status.HTTP_201_CREATED)