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

    def save(self, surveyNumber, surveyQuestionNumber, surveySelectionNumber):
        surveyDocument = SurveyDocument.objects.get(id=surveyNumber)
        survey = Survey.objects.get(SurveyDocumentID=surveyDocument)
        surveyQuestion = SurveyQuestion.objects.get(SurveyID=surveyNumber)
        surveySelection = SurveySelection.objects.get(SurveyQuestionID=surveyQuestionNumber.id)

        SurveyAnswer.objects.create(
            SurveyQuestionID=surveyQuestionNumber.id,
            SurveySelectionID=surveySelectionNumber.id
        )

    def findDocumentById(self, Id):
        return SurveyDocument.objects.get(id=Id)

    def findSurveyByDocument(self, document):
        return Survey.objects.get(SurveyDocumentID=document)

    def findQuestionBySurvey(self, survey):
        return SurveyQuestion.objects.filter(SurveyID=survey)

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
        for question in surveyQuestionSentence:
            q = SurveyQuestion.objects.create(
                SurveyID=survey,
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

    def returnComponents(self, surveyNumber):
        try:
            surveyDocumentID = SurveyDocument.objects.get(id=surveyNumber)
        except Exception as e:
            print('error occurred while getting surveyDocumentID:', e)

        surveyID = Survey.objects.get(SurveyDocumentID=surveyDocumentID.id)
        surveyQuestions = SurveyQuestion.objects.filter(SurveyID=surveyID.id).order_by('id')
        surveyQuestionList = [component.SurveyQuestionSentence for component in surveyQuestions]
        print(surveyQuestionList)

        surveySelectionDoubleList = []
        for component in surveyQuestions:
            surveySelections = SurveySelection.objects.filter(SurveyQuestionID=component.id).order_by('id')
            surveySelectionList = [component.SurveySelectionSentence for component in surveySelections]
            surveySelectionDoubleList.append(surveySelectionList)
        print(surveySelectionDoubleList)

        return surveyQuestionList, surveySelectionDoubleList
