import os

import pandas
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
        print("controller -> saveSurveyAnswer()")
        try:
            surveyNumber = request.data.get("surveyId")
            surveySelectionNumber = request.data.get("answer")

            if not surveyNumber or not surveySelectionNumber:
                return Response({'response': 'There is no content'}, status=status.HTTP_204_NO_CONTENT)

            self.surveyService.saveSurveyAnswer(surveyNumber, surveySelectionNumber)

            return Response({'response': True}, status=status.HTTP_200_OK)
        except Exception as e:
            print("error occurred while saving survey answer:", e)
            return Response({'response': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def read(self, request, surveyId=None):
        questionList, selectionList = self.surveyService.readSurvey(surveyId)

        return Response({'surveyId': surveyId, 'questions': questionList, 'selections': selectionList},
                        status=status.HTTP_200_OK)

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

    def readSurveyResult(self, request):
        print("readSurveyResult()")
        try:
            surveyNumber = request.data.get("surveyNumber")

            if not surveyNumber:
                return Response({'response': 'There is no content received'}, status=status.HTTP_204_NO_CONTENT)

            questionList, selectionList, selectionQuantity = self.surveyService.readSurveyResult(surveyNumber)

            return Response(
                {'questionList': questionList, 'selectionList': selectionList, "selectionQuantity": selectionQuantity},
                status=status.HTTP_200_OK)

        except Exception as e:
            print('error occurred while abstracting survey result!: ', e)
            return Response({'response': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def saveFirstSurveyCSVData(self, request):
        print("saveFirstSurveyCSVData")
        try:
            if request.data.get('password') == os.getenv('PASSWORD'):
                file = pandas.read_csv(request.data.get("file"), encoding='utf-8')

                questionList = list(file.columns)
                answerList = []
                for i, row in file.iterrows():
                    answerList.append(tuple(row))

                bulkInjectionList = self.surveyService.makeBulkInjection(questionList, answerList)
                self.surveyService.operateBulkInjection(bulkInjectionList)

                return Response({'response': True}, status=status.HTTP_200_OK)
            else:
                print("not authorized request!")
                return Response({'response': False}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

        except Exception as e:
            print("error occurred while saving csv data!: ", e)
            return Response({'response': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
