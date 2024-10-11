from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_team_member.controller.views import ResultReportTeamMemberView

router = DefaultRouter()
router.register(r"report_team_member", ResultReportTeamMemberView, basename="report_team_member")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportTeamMemberView.as_view({"post": "createResultReportTeamMember"}), name="create-result-report-team-member"),
]