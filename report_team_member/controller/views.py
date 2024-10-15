from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from report_team_member.entity.report_team_member import ResultReportTeamMember
from report_team_member.service.report_team_member_service_impl import ResultReportTeamMemberServiceImpl


# Create your views here.
class ResultReportTeamMemberView(viewsets.ViewSet):
    queryset = ResultReportTeamMember.objects.all()
    resultReportTeamMemberService = ResultReportTeamMemberServiceImpl.getInstance()

    def createResultReportTeamMember(self, request):
        data = request.data
        name = data.get("name")
        role = data.get("role")
        resultReportTeamId = data.get("resultReportTeamId")

        self.resultReportTeamMemberService.createResultReportTeamMember(name, role, resultReportTeamId)

        return Response(status=status.HTTP_201_CREATED)