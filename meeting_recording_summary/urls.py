from django.urls import path, include
from rest_framework.routers import DefaultRouter

from meeting_recording_summary.controller.views import MeetingRecordingSummaryView

router = DefaultRouter()
router.register(r"meeting_recording_summary", MeetingRecordingSummaryView, basename="meeting_recording_summary")

urlpatterns = [
    path("", include(router.urls)),
    path("create", MeetingRecordingSummaryView.as_view({"post": "create"}), name="create-meeting-recording-summary"),
    path("list", MeetingRecordingSummaryView.as_view({"post": "list"}), name="list-meeting-recording-summary"),
    path("read/<int:meetingRecordingSummaryId>", MeetingRecordingSummaryView.as_view({"post", "read"}), name="read-meeting-recording-summary"),
]