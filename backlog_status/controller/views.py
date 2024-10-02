from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from backlog_status.service.backlog_status_service_impl import BacklogStatusServiceImpl


class BacklogStatusView(viewsets.ViewSet):
    backlogStatusService = BacklogStatusServiceImpl.getInstance()

    def createBacklogStatus(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        backlogStatus = data.get('status')

        createdBacklogStatus = self.backlogStatusService.createBacklogStatus(backlogId, backlogStatus)

        return Response(createdBacklogStatus, status=status.HTTP_200_OK )