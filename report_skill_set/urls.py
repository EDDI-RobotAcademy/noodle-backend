from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_skill_set.controller.views import ResultReportSkillSetView

router = DefaultRouter()
router.register(r"report_skill_set", ResultReportSkillSetView, basename="report_skill_set")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportSkillSetView.as_view({"post": "createResultReportSkillSet"}), name="create-result-report-skill-set"),
]