from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from commits.service.commits_service_impl import CommitsServiceImpl
from github_oauth.service.redis_service_impl import RedisServiceImpl


class CommitsView(viewsets.ViewSet):
    commitsService = CommitsServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def save(self, request):
        userToken = request.data['userToken']
        reponame = request.data['reponame']
        branchname = request.data['branchname']

        accountId = self.redisService.getValueByKey(userToken)
        accessToken = self.redisService.getValueByKey(accountId)

        self.commitsService.save(accountId, accessToken, reponame, branchname)

        return Response(status=status.HTTP_200_OK)

    def list(self, request):
        userToken = request.data['userToken']
        reponame = request.data['reponame']
        branchname = request.data['branchname']
        page = request.data['page']

        accountId = self.redisService.getValueByKey(userToken)

        commitList = self.commitsService.getAllCommits(accountId, reponame, branchname, page)

        return Response({"commit_list": commitList}, status=HTTP_200_OK)
