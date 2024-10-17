from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_feature_content.controller.views import ResultReportFeatureContentView

router = DefaultRouter()
router.register(r"report_feature_content", ResultReportFeatureContentView, basename="report_feature_content")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportFeatureContentView.as_view({"post": "create"}), name="create-result-report-feature-content"),
]