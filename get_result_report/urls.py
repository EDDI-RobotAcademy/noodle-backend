from django.urls import path, include
from rest_framework.routers import DefaultRouter

from get_result_report.controller.views import GetResultReportView

router = DefaultRouter()
router.register(r'get_result_report', GetResultReportView, basename='ai-get_result_report')

urlpatterns = [
    path('', include(router.urls)),
    path('get', GetResultReportView.as_view({'post': 'getResultReportToFastAPI'}), name='get-result-report'),
]