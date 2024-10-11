from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from report_team.entity.report_team import ResultReportTeam
from report_team.service.report_team_service_impl import ResultReportTeamServiceImpl


# Create your views here.
class ResultReportTeamView(viewsets.ViewSet):
    queryset = ResultReportTeam.objects.all()
    resultReportTeamService = ResultReportTeamServiceImpl.getInstance()

    def createResultReportTeam(self, request):
        data = request.data
        resultReportId = data.get("resultReportId")
        self.resultReportTeamService.createResultReportTeam(resultReportId)

        return Response(status=status.HTTP_201_CREATED)
