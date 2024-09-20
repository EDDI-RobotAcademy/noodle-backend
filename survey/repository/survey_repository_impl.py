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
        surveyQuestion = SurveyQuestion.objects.get(SurveyID=surveyNumber)
        surveyQuestionNumber = surveyQuestion.objects.get(SurveyQuestionNumber=surveyQuestionNumber)
        surveySelection = SurveySelection.objects.get(SurveyQuestionID=surveyQuestionNumber.id)
        surveySelectionNumber = surveySelection.objects.get(SurveySelectionNumber=surveySelectionNumber)

        SurveyAnswer.objects.create(
            SurveyQuestionID=surveyQuestionNumber.id,
            SurveySelectionID=surveySelectionNumber.id
        )

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
                    SurveySelectionNumber=j+1,
                    SurveySelectionSentence=surveySelectionList[i][j]
                )

        return survey