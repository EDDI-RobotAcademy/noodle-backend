import json

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from backlog.service.backlog_service_impl import BacklogServiceImpl
from github_oauth.service.redis_service_impl import RedisServiceImpl


class BacklogView(viewsets.ViewSet):
    backlogService = BacklogServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def createBacklog(self, request):
        data = request.data
        userToken = data.get('userToken')
        backlogList = data.get('intermediateData')

        if not backlogList:
            return Response({"error": "제목이 필요합니다"}, status=status.HTTP_400_BAD_REQUEST)

        createdBacklog, idxList = self.backlogService.createBacklog(backlogList)

        self.redisService.setBacklogCreationFlag(userToken, idxList)

        return Response(f"Success to create {len(createdBacklog)} number of backlogs!", status=status.HTTP_200_OK)

    def getBacklog(self, request):
        try:
            data = request.data
            userToken = data.get("userToken")

            if not userToken:
                return Response({'error': "invalid token!"}, status=status.HTTP_401_UNAUTHORIZED)

            value = self.redisService.getBacklogCreationFlag(userToken)

            if value == 0:
                return Response({'error': "creation is not done yet!"}, status=status.HTTP_102_PROCESSING)
            else:
                values = json.loads(value)
                backlogs = self.backlogService.getBacklogs(values.get("startIdx"), values.get("endIdx"))
                return Response({'response': backlogs}, status=status.HTTP_200_OK)

        except Exception as e:
            print('error while getting backlogs: ', e)
            return Response({'error': "backlog load failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
