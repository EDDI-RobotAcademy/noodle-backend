from rest_framework import serializers


class GithubOauthUrlSerializer(serializers.Serializer):
    url = serializers.URLField()
