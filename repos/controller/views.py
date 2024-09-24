from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from repos.service.repos_service_impl import ReposServiceImpl


class ReposView(viewsets.ViewSet):
    reposService = ReposServiceImpl.getInstance()

    def list(self, request):
        print("service -> list()")
        accessToken = request.data['access_token']
        username = request.data['nickname']

        repoList = self.reposService.list(username, accessToken)

        return Response({"repo_list": repoList}, status=status.HTTP_200_OK)
