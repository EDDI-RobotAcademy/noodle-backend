from django.urls import path, include
from rest_framework.routers import DefaultRouter

from commits.controller.views import CommitsView

router = DefaultRouter()
router.register(r"commits", CommitsView, basename="commits")

urlpatterns = [
    path("", include(router.urls)),
    path("list", CommitsView.as_view({"get": "list"}), name="get-commits-of-page"),
]