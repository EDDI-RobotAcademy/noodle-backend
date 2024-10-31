from django.urls import path, include
from rest_framework.routers import DefaultRouter

from get_meeting_recording_summary.controller.views import GetMeetingRecordingSummaryView

router = DefaultRouter()
router.register(r"get_meeting_recording_summary", GetMeetingRecordingSummaryView, basename="get_meeting_recording_summary")

urlpatterns = [
    path('', include(router.urls)),
    path('get', GetMeetingRecordingSummaryView.as_view({'post': "getMeetingRecordingSummaryToFastAPI"}), name='get-meeting-recording-summary'),
]