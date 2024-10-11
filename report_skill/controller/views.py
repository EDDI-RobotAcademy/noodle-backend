from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from report_skill.entity.report_skill import ResultReportSkill
from report_skill.service.report_skill_service_impl import ResultReportSkillServiceImpl


# Create your views here.
class ResultReportSkillView(viewsets.ViewSet):
    queryset = ResultReportSkill.objects.all()
    resultReportSkillService = ResultReportSkillServiceImpl.getInstance()

    def createResultReportSkill(self, request):
        data = request.data
        skill = data.get("skill")
        skillSetId = data.get("skillSetId")

        self.resultReportSkillService.createResultReportSkill(skill, skillSetId)

        return Response(status=status.HTTP_201_CREATED)
