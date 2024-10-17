from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_feature.controller.views import ResultReportFeatureView

router = DefaultRouter()
router.register(r"report_feature", ResultReportFeatureView, basename="report_feature")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportFeatureView.as_view({"post": "create"}), name="create-result-report-feature"),
]