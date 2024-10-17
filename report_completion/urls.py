from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_completion.controller.views import ResultReportCompletionView

router = DefaultRouter()
router.register(r"report_completion", ResultReportCompletionView, basename="report_completion")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportCompletionView.as_view({"post": "create"}), name="create-result-report-completion"),
]
