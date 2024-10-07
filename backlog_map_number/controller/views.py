from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from backlog_map_number.service.backlog_map_number_service_impl import BacklogMapNumberServiceImpl


class BacklogMapNumberView(viewsets.ViewSet):
    backlogMapNumberService = BacklogMapNumberServiceImpl.getInstance()

    def createBacklogMapNumber(self, request):
        data = request.data
        backlogId = data.get("backlogId")
        backlogMapNumber = data.get("backlog_map_number")

        createBacklogMapNumber = self.backlogMapNumberService.createBacklogMapNumber(backlogId, backlogMapNumber).mapNumber

        return Response(createBacklogMapNumber, status=status.HTTP_200_OK)