from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from github_oauth.serializers.github_oauth_access_token_serializer import GithubOauthAccessTokenSerializer
from github_oauth.serializers.github_oauth_url_serializer import GithubOauthUrlSerializer
from github_oauth.service.github_oauth_service_impl import GithubOauthServiceImpl


class OauthView(viewsets.ViewSet):
    githubOauthService = GithubOauthServiceImpl.getInstance()

    def githubOauthURI(self, request):
        url = self.githubOauthService.githubLoginAddress()
        print(f"url: {url}")
        serializer = GithubOauthUrlSerializer(data={'url': url})
        serializer.is_valid(raise_exception=True)
        print(f"validated_data: {serializer.validated_data}")
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def githubAccessTokenURL(self, request):
        serializer = GithubOauthAccessTokenSerializer(code=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']

        try:
            accessToken = self.githubOauthService.requestAccessToken(code)
            print(f"accessToken: {accessToken}")
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
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
