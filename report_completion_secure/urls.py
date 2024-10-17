from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_completion_secure.controller.views import ResultReportCompletionSecureView

router = DefaultRouter()
router.register(r"report_completion_secure", ResultReportCompletionSecureView, basename="report_completion_secure")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportCompletionSecureView.as_view({"post": "create"}), name="create-result-report-completion-secure"),
]