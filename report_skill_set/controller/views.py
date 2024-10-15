from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from report_skill_set.entity.report_skill_set import ResultReportSkillSet
from report_skill_set.service.report_skill_set_service_impl import ResultReportSkillSetServiceImpl


# Create your views here.
class ResultReportSkillSetView(viewsets.ViewSet):
    queryset = ResultReportSkillSet.objects.all()
    resultReportSkillSetService = ResultReportSkillSetServiceImpl.getInstance()

    def createResultReportSkillSet(self, request):
        data = request.data
        resultReportId = data.get("resultReportId")

        self.resultReportSkillSetService.createResultReportSkillSet(resultReportId)

        return Response(status=status.HTTP_201_CREATED)
