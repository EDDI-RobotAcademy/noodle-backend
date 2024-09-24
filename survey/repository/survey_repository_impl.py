from requests import Response

from survey.entity.survey import Survey
from survey.entity.survey_answer import SurveyAnswer
from survey.entity.survey_document import SurveyDocument
from survey.entity.survey_question import SurveyQuestion
from survey.entity.survey_selection import SurveySelection
from survey.repository.survey_repository import SurveyRepository


class SurveyRepositoryImpl(SurveyRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def findDocumentById(self, Id):
        return SurveyDocument.objects.get(id=Id)

    def findSurveyByDocument(self, document):
        return Survey.objects.get(SurveyDocumentID=document)

    def findQuestionBySurvey(self, survey):
        return SurveyQuestion.objects.filter(SurveyID=survey).order_by('id')

    def findSelectionByQuestion(self, question):
        selections = []
        for q in question:
            selection = SurveySelection.objects.filter(SurveyQuestionID=q)
            selections.append(selection)

        return selections

    def register(self, surveyID, surveyQuestionSentence, surveySelectionList):
        print("repository -> register()")
        try:
            surveyDocumentID = SurveyDocument.objects.get(id=surveyID)
            survey = Survey.objects.get(SurveyDocumentID=surveyDocumentID)
        except SurveyDocument.DoesNotExist:
            surveyDocumentID = SurveyDocument.objects.create()
            survey = Survey.objects.create(SurveyDocumentID=surveyDocumentID)

        questionList = []
        cnt = 0
        for question in surveyQuestionSentence:
            cnt += 1
            q = SurveyQuestion.objects.create(
                SurveyID=survey,
                SurveyQuestionNumber=cnt,
                SurveyQuestionSentence=question,
            )
            questionList.append(q)

        for i in range(len(questionList)):
            for j in range(len(surveySelectionList[i])):
                SurveySelection.objects.create(
                    SurveyQuestionID=questionList[i],
                    SurveySelectionNumber=j + 1,
                    SurveySelectionSentence=surveySelectionList[i][j]
                )

        return survey

    def returnComponents(self, surveyNumber, flag):
        try:
            surveyDocumentID = SurveyDocument.objects.get(id=surveyNumber)
        except Exception as e:
            print('error occurred while getting surveyDocumentID:', e)

        surveyID = Survey.objects.get(SurveyDocumentID=surveyDocumentID.id)
        surveyQuestions = SurveyQuestion.objects.filter(SurveyID=surveyID.id).order_by('id')
        surveyQuestionList = [component.SurveyQuestionSentence for component in surveyQuestions]
        print(surveyQuestionList)

        surveySelectionDoubleList = []
        surveyQuantityDoubleList = []
        for component in surveyQuestions:
            surveySelections = SurveySelection.objects.filter(SurveyQuestionID=component.id).order_by('id')
            surveySelectionList = [component.SurveySelectionSentence for component in surveySelections]
            surveySelectionDoubleList.append(surveySelectionList)
            if flag == 1:
                surveyQuantityList = []
                surveySelectionComponentList = [component for component in surveySelections]
                for surveySelection in surveySelectionComponentList:
                    surveySelectionQuantity = SurveyAnswer.objects.filter(SurveySelectionID=surveySelection).count()
                    surveyQuantityList.append(surveySelectionQuantity)
                surveyQuantityDoubleList.append(surveyQuantityList)
        print(surveySelectionDoubleList)

        if flag == 1:
            print(surveyQuantityDoubleList)
            return surveyQuestionList, surveySelectionDoubleList, surveyQuantityDoubleList

        return surveyQuestionList, surveySelectionDoubleList

    def findSelectionBySurveyQuestionIDAndSelectionNumber(self, questionID, selectionNumber):
        return SurveySelection.objects.get(SurveyQuestionID=questionID, SurveySelectionNumber=selectionNumber)

    def list(self):
        return SurveyDocument.objects.all()


    def findQuestionByQuestionSentence(self, questionSentence):
        return SurveyQuestion.objects.get(SurveyQuestionSentence=questionSentence)

    def findSelectionBySelectionSentence(self, questionID, answer):
        return SurveySelection.objects.get(SurveyQuestionID=questionID, SurveySelectionSentence=answer)

    def operateBulkInjection(self, bulkInjectionQueryList):
        SurveyAnswer.objects.bulk_create(bulkInjectionQueryList)
