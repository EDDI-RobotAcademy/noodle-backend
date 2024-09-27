from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from branches.service.branches_service_impl import BranchesServiceImpl
from github_oauth.service.redis_service_impl import RedisServiceImpl


class BranchesView(viewsets.ViewSet):
    branchesService = BranchesServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def save(self, request):
        try:
            userToken = request.data.get('userToken')
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        reponame = request.data.get('reponame')
        accountId = self.redisService.getValueByKey(userToken)
        accessToken = self.redisService.getValueByKey(accountId)

        self.branchesService.save(accountId, accessToken, reponame)

        return Response(status=status.HTTP_200_OK)

    def list(self, request):
        try:
            userToken = request.data.get('userToken')
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        reponame = request.data.get('reponame')
        accountId = self.redisService.getValueByKey(userToken)

        branchList = self.branchesService.list(accountId, reponame)

        return Response({"branch_list": branchList}, status=status.HTTP_200_OK)
