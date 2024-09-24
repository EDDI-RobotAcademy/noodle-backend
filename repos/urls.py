from django.urls import path, include
from rest_framework.routers import DefaultRouter

from repos.controller.views import ReposView

router = DefaultRouter()
router.register(r"repos", ReposView, basename="repos")

urlpatterns = [
    path('', include(router.urls)),
    path('list', ReposView.as_view({"get": "list"}), name="get-all-repositories"),
]