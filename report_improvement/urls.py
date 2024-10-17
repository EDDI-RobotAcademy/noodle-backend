from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_improvement.controller.views import ResultReportImprovementView

router = DefaultRouter()
router.register(r"report_improvement", ResultReportImprovementView, basename="report_improvement")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportImprovementView.as_view({"post": "create"}), name="create-result-report-improvement"),
]