from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_overview.controller.views import ResultReportOverviewView

router = DefaultRouter()
router.register(r"report_overview", ResultReportOverviewView, basename="report_overview")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportOverviewView.as_view({"post": "create"}), name="create-result-report-overview"),
]