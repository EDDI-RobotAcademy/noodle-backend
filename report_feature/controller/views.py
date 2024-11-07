from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from report_feature.entity.report_feature import ResultReportFeature
from report_feature.service.report_feature_service_impl import ResultReportFeatureServiceImpl


# Create your views here.
class ResultReportFeatureView(viewsets.ViewSet):
    queryset = ResultReportFeature.objects.all()
    resultReportFeatureService = ResultReportFeatureServiceImpl.getInstance()

    def create(self, request):
        data = request.data
        resultReportId = data.get('resultReportId')

        self.resultReportFeatureService.create(resultReportId)

        return Response(status=status.HTTP_201_CREATED)
