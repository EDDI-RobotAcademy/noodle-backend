from django.urls import path, include
from rest_framework.routers import DefaultRouter

from branches.controller.views import BranchesView

router = DefaultRouter()
router.register(f'branches', BranchesView, basename="branches")

urlpatterns = [
    path('', include(router.urls)),
    path('list', BranchesView.as_view({"get": "list"}), name="get-all-branches"),
]