from abc import ABC, abstractmethod

class GithubOauthService(ABC):
    @abstractmethod
    def githubLoginAddress(self):
        pass

    @abstractmethod
    def requestAccessToken(self, githubAuthCode):
        pass

    @abstractmethod
    def requestUserInfo(self, accessToken):
        pass