from rest_framework import viewsets, status
from rest_framework.response import Response

from survey.service.survey_service_impl import SurveyServiceImpl


class SurveyView(viewsets.ViewSet):
    surveyService = SurveyServiceImpl.getInstance()

    def registerNewSurvey(self, request):
        print('createNewSurvey()')
        try:
            surveyID = request.data.get("surveyId")
            surveyQuestionSentence = request.data.get("questions")  # list
            print("surveyQuestionSentence:", surveyQuestionSentence)
            surveySelectionList = request.data.get("answers")  # list(list)
            print("surveySelectionList:", surveySelectionList)

            if not surveyID or not surveyQuestionSentence or not surveySelectionList:
                return Response({'response': 'There is no content'}, status=status.HTTP_204_NO_CONTENT)

            survey = self.surveyService.registerNewSurvey(surveyID, surveyQuestionSentence,
                                                          surveySelectionList)

            return Response({'response': survey.SurveyDocumentID.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("error occurred while registering survey :", e)
            return Response({'response': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def saveSurveyAnswer(self, request):
        print("saveSurveyAnswer()")
        try:
            surveyNumber = request.data.get("surveyNumber")
            surveyQuestionNumber = request.data.get("surveyQuestionNumber")
            surveySelectionNumber = request.data.get("surveySelectionNumber")

            if not surveyNumber or not surveyQuestionNumber or not surveySelectionNumber:
                return Response({'response': 'There is no content'}, status=status.HTTP_204_NO_CONTENT)

            self.surveyService.saveSurveyAnswer(surveyNumber, surveyQuestionNumber, surveySelectionNumber)

            return Response({'response': True}, status=status.HTTP_200_OK)
        except Exception as e:
            print("error occurred while saving servey answer")
            return Response({'response': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def read(self, request, surveyId=None):
        questionList, selectionList = self.surveyService.readSurvey(surveyId)

        return Response({'surveyId': surveyId, 'questions': questionList, 'selections': selectionList}, status=status.HTTP_200_OK)
    def returnSurveyComponents(self, request):
        print("returnSurveyComponents()")
        try:
            surveyNumber = request.data.get("surveyNumber")

            if not surveyNumber:
                return Response({'response': 'There is no content received'}, status=status.HTTP_204_NO_CONTENT)

            questionComponents, selectionComponents = self.surveyService.returnSurveyComponents(surveyNumber)

            return Response({'questionComponents': questionComponents, 'selectionComponents': selectionComponents},
                            status=status.HTTP_200_OK)
        except Exception as e:
            print('error occurred while creating response Components!:', e)
            return Response({'response': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
