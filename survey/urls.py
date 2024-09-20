from django.urls import path, include
from rest_framework.routers import DefaultRouter

from survey.controller.views import SurveyView

router = DefaultRouter()
router.register(r'', SurveyView, basename='survey')

urlpatterns = [
    path('', include(router.urls)),
    path('save', SurveyView.as_view({'post': 'saveSurveyAnswer'}), name='save-survey-answer'),
    path('register', SurveyView.as_view({'post': 'registerNewSurvey'}), name='register-new-survey'),
    path('read/<int:surveyId>', SurveyView.as_view({'get': 'read'}), name='read-survey'),
    path('register', SurveyView.as_view({'post': 'registerNewSurvey'}), name='register-new-survey'),
    path('return-survey-components', SurveyView.as_view({'post': 'returnSurveyComponents'}),
         name='return-survey-components'),
]
