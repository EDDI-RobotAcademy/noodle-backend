import uuid

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.service.account_service_impl import AccountServiceImpl
from github_oauth.serializers.github_oauth_access_token_serializer import GithubOauthAccessTokenSerializer
from github_oauth.serializers.github_oauth_url_serializer import GithubOauthUrlSerializer
from github_oauth.service.github_oauth_service_impl import GithubOauthServiceImpl


class OauthView(viewsets.ViewSet):
    githubOauthService = GithubOauthServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def githubOauthURI(self, request):
        url = self.githubOauthService.githubLoginAddress()
        print(f"url: {url}")
        serializer = GithubOauthUrlSerializer(data={'url': url})
        serializer.is_valid(raise_exception=True)
        print(f"validated_data: {serializer.validated_data}")
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def githubAccessTokenURL(self, request):
        serializer = GithubOauthAccessTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']

        try:
            accessToken = self.githubOauthService.requestAccessToken(code)
            print(f"accessToken: {accessToken}")
            return Response({"code": accessToken['access_token']}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def githubUserInfoURL(self, request):
        accessToken = request.data.get('access_token')
        print(f'accessToken: {accessToken}')

        try:
            userInfo = self.githubOauthService.requestUserInfo(accessToken)
            return Response({'user_info': userInfo}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def redisAccessToken(self, request):
        try:
            username = request.data.get('username')
            access_token = request.data.get('accessToken')
            print(f"redisAccessToken -> username: {username}")

            account = self.accountService.findAccountByUsername(username)
            if not account:
                return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

            userToken = str(uuid.uuid4())
            self.redisService.store_access_token(account.id, userToken)
            self.redisService.store_access_token(access_token, account.id)


            return Response({'userToken': userToken}, status=status.HTTP_200_OK)
        except Exception as e:
            print('Error storing access token in Redis:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

