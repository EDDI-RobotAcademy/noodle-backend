from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_improvement_content.controller.views import ResultReportImprovementContentView

router = DefaultRouter()
router.register(r"report_improvement_content", ResultReportImprovementContentView, basename="report_improvement_content")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportImprovementContentView.as_view({"post": "create"}), name="create-result-report-improvement-content"),
]