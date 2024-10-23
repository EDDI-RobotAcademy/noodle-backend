from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from backlog.service.backlog_service_impl import BacklogServiceImpl


class BacklogView(viewsets.ViewSet):
    backlogService = BacklogServiceImpl.getInstance()

    def createBacklog(self, request):
        data = request.data
        userToken = data.get('userToken')
        result = data.get('aiResult')
        backlogList = result['backlog']

        if not backlogList:
            return Response({"error": "제목이 필요합니다"}, status=status.HTTP_400_BAD_REQUEST)

        createdBacklog = self.backlogService.createBacklog(backlogList).title

        return Response(createdBacklog, status=status.HTTP_200_OK)