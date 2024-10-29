from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from ai_request.service.ai_request_service_impl import AIRequestServiceImpl
from github_oauth.service.redis_service_impl import RedisServiceImpl


# Create your views here.
class AIRequestView(viewsets.ViewSet):
    redisService = RedisServiceImpl.getInstance()
    AIRequestService = AIRequestServiceImpl.getInstance()

    def aiRequestToFastAPI(self, request):
        data = request.data
        userToken = data.get('userToken')
        command = data.get('command')
        data = data.get('data')

        try:
            accountId = self.redisService.getValueByKey(userToken)
        except Exception as e:
            print("aiRequestToFastAPI() 중 에러 발생:", e)
            raise e

        requestComplete = self.AIRequestService.aiRequestToFastAPI(userToken, accountId, command, data)

        return Response(requestComplete, status=status.HTTP_200_OK)