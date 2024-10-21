from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account.controller.views import AccountView

router = DefaultRouter()
router.register("account", AccountView, basename="account")

urlpatterns = [
    path("", include(router.urls)),
    path("check-username-duplicate", AccountView.as_view({"post": "checkUserNameDuplication"}), name="check-username-duplicate"),
    path("get-username-by-user-token", AccountView.as_view({"post": "getUserNameByUserToken"}), name="get-username-by-user-token"),
]