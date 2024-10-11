from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_skill.controller.views import ResultReportSkillView

router = DefaultRouter()
router.register(r"report_skill", ResultReportSkillView, basename="report_skill")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportSkillView.as_view({"post": "createResultReportSkill"}), name="create-result-report-skill"),
]