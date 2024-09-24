from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from commits.service.commits_service_impl import CommitsServiceImpl


class CommitsView(viewsets.ViewSet):
    commitsService = CommitsServiceImpl.getInstance()

    def list(self, request):
        username = request.data['username']
        reponame = request.data['reponame']
        accessToken = request.data['access_token']
        branchname = request.data['branchname']
        pageNumber = request.data['page_number']

        commitList = self.commitsService.list(username, accessToken, reponame, branchname, pageNumber)

        return Response({"commit_list": commitList}, status=status.HTTP_200_OK)
