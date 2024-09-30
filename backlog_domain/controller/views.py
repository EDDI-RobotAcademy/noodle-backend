from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

class BacklogDomainView(viewsets.ViewSet):
    backlogDomainService = BacklogDomainServiceImpl.getInstance()

    def createBacklogDomain(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        domain = data.get('domain')

        createdBacklogDomain = backlogDomainService.createBacklogDomain(backlogId, domain)

        return Response(createdBacklogDomain, status=status.HTTP_200_OK)