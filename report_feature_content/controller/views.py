from django.shortcuts import render
from rest_framework import viewsets

from report_feature_content.entity.report_feature_content import ResultReportFeatureContent


# Create your views here.
class ResultReportFeatureContentView(viewsets.ViewSet):
    queryset = ResultReportFeatureContent.objects.all()
    resultReportFeatureContentService = ResultReportFeatureContentServiceImpl.getInstance()

    def create(self, request):
        data = request.data
        resultReportId = data.get("resultReportId")

        self.resultReportFeatureContentService.create(resultReportId)
