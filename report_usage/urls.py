from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_usage.controller.views import ResultReportUsageView

router = DefaultRouter()
router.register(r"report_usage", ResultReportUsageView, basename="report_usage")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportUsageView.as_view({"post": "create"}), name='create-result-report-usage'),
]