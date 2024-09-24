from rest_framework import serializers


class GithubOauthAccessTokenSerializer(serializers.Serializer):
    code = serializers.CharField()