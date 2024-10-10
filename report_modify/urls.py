from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_modify.controller.views import ResultReportModifyView

router = DefaultRouter()
router.register(r"report_modify", ResultReportModifyView, basename="report_modify")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportModifyView.as_view({"put": "createResultReportModify"}), name="create-result-report-modify"),
]