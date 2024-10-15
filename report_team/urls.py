from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_team.controller.views import ResultReportTeamView

router = DefaultRouter()
router.register(r"report_team", ResultReportTeamView, basename="report_team")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportTeamView.as_view({"post": "createResultReportTeam"}), name="create-result-report-team"),
]
