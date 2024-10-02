from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from backlog.service.backlog_service_impl import BacklogServiceImpl
from backlog_issue.service.backlog_issue_service_impl import BacklogIssueServiceImpl


class BacklogIssueView(viewsets.ViewSet):
    backlogService = BacklogServiceImpl.getInstance()
    backlogIssueService = BacklogIssueServiceImpl.getInstance()

    def createBacklogIssue(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        issue = data.get('issue')

        createdBacklogIssue = self.backlogIssueService.createBacklogIssue(backlogId, issue)

        return Response(createdBacklogIssue, status=status.HTTP_200_OK)

    def modifyBacklogIssue(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        domain = data.get('domain')

        modifiedBacklogIssue = self.backlogIssueService.modifyBacklogIssue(backlogId, domain)

        return Response(modifiedBacklogIssue, status=status.HTTP_200_OK)