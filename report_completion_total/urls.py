from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_completion_total.controller.views import ResultReportCompletionTotalView

router = DefaultRouter()
router.register(r"report_completion_total", ResultReportCompletionTotalView, basename="report_completion_total")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportCompletionTotalView.as_view({"post": "create"}), name="create-result-report-completion-total"),
]