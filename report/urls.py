from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report.controller.views import ResultReportView

router = DefaultRouter()
router.register(r"report", ResultReportView, basename="report")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportView.as_view({"post": "createResultReport"}), name="create-result-report"),
    path("list", ResultReportView.as_view({"post": "list"}), name="list-result-report"),
    path("read", ResultReportView.as_view({'post': "read"}), name="result-report-read"),
    path("modify", ResultReportView.as_view({'post': "modify"}), name="result-report-modify"),
    path('delete', ResultReportView.as_view({'post': 'delete'}), name="result-report-delete"),
    path('validate', ResultReportView.as_view({'post': 'validation'}), name="modifier-validation"),
]
