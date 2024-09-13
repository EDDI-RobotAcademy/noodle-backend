from rest_framework import viewsets, status
from rest_framework.response import Response

from survey.service.survey_service_impl import SurveyServiceImpl


class SurveyView(viewsets.ViewSet):
    surveyService = SurveyServiceImpl.getInstance()

    def registerNewSurvey(self, request):
        print('createNewSurvey()')
        try:
            surveyID = request.data.get("surveyID")
            surveyQuestionNumber = request.data.get("surveyQuestionNumber")
            surveyQuestionSentence = request.data.get("surveyQuestionSentence")
            surveySelectionList = request.data.get("surveySelectionList")

            self.surveyService.registerNewSurvey(surveyID, surveyQuestionNumber, surveyQuestionSentence,
                                                 surveySelectionList)

            return Response({'response': True}, status=status.HTTP_200_OK)
        except Exception as e:
            print("error occured while registering survey :", e)
            return Response({'response': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def saveSurveyAnswer(self, request):
        print("saveSurveyAnswer()")
        try:
            surveyNumber = request.data.get("surveyNumber")
            surveyQuestionNumber = request.data.get("surveyQuestionNumber")
            surveySelectionNumber = request.data.get("surveySelectionNumber")

            self.surveyService.saveSurveyAnswer(surveyNumber, surveyQuestionNumber, surveySelectionNumber)

            return Response({'response': True}, status=status.HTTP_200_OK)
        except Exception as e:
            print("error occured while saving servey answer")
            return Response({'response': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
