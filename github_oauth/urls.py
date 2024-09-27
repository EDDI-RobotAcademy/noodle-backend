from django.urls import path, include
from rest_framework.routers import DefaultRouter

from github_oauth.controller.views import OauthView

router = DefaultRouter()
router.register(f'github_oauth', OauthView, basename='github_oauth')

urlpatterns = [
    path('', include(router.urls)),
    path('github', OauthView.as_view({'get': 'githubOauthURI'}), name='get-github-oauth-uri'),
    path('github/access-token', OauthView.as_view({'post': 'githubAccessTokenURL'}), name="get-github-access-token-url"),
    path('github/logout', OauthView.as_view({'post': 'dropRedisTokenForLogout'}), name="github-logout")
]