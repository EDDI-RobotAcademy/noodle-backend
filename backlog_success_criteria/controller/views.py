from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from backlog_success_criteria.service.backlog_success_criteria_service_impl import BacklogSuccessCriteriaServiceImpl


class BacklogSuccessCriteriaView(viewsets.ViewSet):
    backlogSuccessCriteriaService = BacklogSuccessCriteriaServiceImpl.getInstance()

    def createBacklogSuccessCriteria(self, request):
        data = request.data
        backlogId = data.get("backlogId")
        successCriteria = data.get("success_criteria")

        createdBacklogSuccessCriteria = self.backlogSuccessCriteriaService.createBacklogSuccessCriteria(backlogId, successCriteria)

        return Response(createdBacklogSuccessCriteria, status=status.HTTP_200_OK)