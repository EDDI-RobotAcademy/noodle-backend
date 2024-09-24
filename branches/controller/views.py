from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from branches.service.branches_service_impl import BranchesServiceImpl


class BranchesView(viewsets.ViewSet):
    branchesService = BranchesServiceImpl.getInstance()

    def list(self, request):
        username = request.data['nickname']
        accessToken = request.data['access_token']
        reponame = request.data['reponame']

        branchesList = self.branchesService.list(username, accessToken, reponame)

        return Response({"branch_list": branchesList}, status=status.HTTP_200_OK)
