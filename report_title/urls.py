from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_title.controller.views import ResultReportTitleView

router = DefaultRouter()
router.register(r"report_title", ResultReportTitleView, basename="report_title")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportTitleView.as_view({"post": "createResultReportTitle"}), name="create-result-report-title"),
]