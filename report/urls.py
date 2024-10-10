from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report.controller.views import ResultReportView

router = DefaultRouter()
router.register(r"report", ResultReportView, basename="report")

urlpatterns = [
    path("", include(router.urls)),
]