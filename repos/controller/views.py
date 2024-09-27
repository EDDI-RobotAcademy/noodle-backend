from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from github_oauth.service.redis_service_impl import RedisServiceImpl
from repos.service.repos_service_impl import ReposServiceImpl


class ReposView(viewsets.ViewSet):
    reposService = ReposServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def save(self, request):
        print("service -> save()")
        try:
            userToken = request.data.get('userToken')
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        accountId = self.redisService.getValueByKey(userToken)
        accessToken = self.redisService.getValueByKey(accountId)
        self.reposService.save(accountId, accessToken)

        return Response(status=status.HTTP_200_OK)

    def list(self, request):
        print("controller -> list()")
        try:
            userToken = request.data.get('userToken')
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        accountId = self.redisService.getValueByKey(userToken)
        repoList = self.reposService.list(accountId)

        return Response({"repo_list": repoList}, status=status.HTTP_200_OK)
