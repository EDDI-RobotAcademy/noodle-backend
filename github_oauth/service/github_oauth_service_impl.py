import requests

from github_oauth.service.github_oauth_service import GithubOauthService
from noodle_project import settings


class GithubOauthServiceImpl(GithubOauthService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.loginUrl = settings.GITHUB['LOGIN_URL']
            cls.__instance.clientId = settings.GITHUB['CLIENT_ID']
            cls.__instance.clientSecret = settings.GITHUB['CLIENT_SECRET']
            cls.__instance.redirectUri = settings.GITHUB['REDIRECT_URI']
            cls.__instance.tokenRequestUrl = settings.GITHUB['TOKEN_REQUEST_URL']
            cls.__instance.userinfoRequestUrl = settings.GITHUB['USERINFO_REQUEST_URL']

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def githubLoginAddress(self):
        print("service -> githubLoginAddress()")
        return (f"{self.loginUrl}?"
                f"client_id={self.clientId}&redirect_uri={self.redirectUri}")

    def requestAccessToken(self, githubAuthCode):
        print("service -> requestAccessToken()")
        accessTokenRequestForm = {
            "client_id": self.clientId,
            "client_secret": self.clientSecret,
            "code": githubAuthCode
        }

        print(f"accessTokenRequestForm: {accessTokenRequestForm}")
        response = requests.post(self.tokenRequestUrl, data=accessTokenRequestForm)
        print(f"response: {response}")

        return response.json()

    def requestUserInfo(self, accessToken):
        headers = {'Authorization': f'Bearer {accessToken}'}
        response = requests.post(self.userinfoRequestUrl, headers=headers)

        return response.json()
