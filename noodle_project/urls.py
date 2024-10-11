"""
URL configuration for noodle_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("survey/", include("survey.urls")),
    path("github-oauth/", include('github_oauth.urls')),
    path("repos/", include("repos.urls")),
    path("branches/", include("branches.urls")),
    path("commits/", include("commits.urls")),
    path("account/", include("account.urls")),
    path("backlog-issue/", include("backlog_issue.urls")),
    path("backlog/", include("backlog.urls")),
    path("backlog-domain/", include("backlog_domain.urls")),
    path("backlog-map-number/", include("backlog_map_number.urls")),
    path("backlog-status/", include("backlog_status.urls")),
    path("backlog-success-criteria/", include("backlog_success_criteria.urls")),
    path("backlog-todo/", include("backlog_todo.urls")),
    path("backlog-todo-check/", include("backlog_todo_check.urls")),
    path("backlog-review/", include("backlog_review.urls")),
    path("review/", include("review.urls")),
    path("report/", include("report.urls")),
    path("report-modify/", include("report_modify.urls")),
    path("report-title/", include("report_title.urls")),
    path("report-team/", include("report_team.urls")),
    path("report-team-member/", include("report_team_member.urls")),
    path("report-skill-set", include("report_skill_set.urls")),
]