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

    def register(self, surveyID, surveyQuestionNumber, surveyQuestionSentence, surveySelectionList):
        if Survey.objects.get(SurveyDocument=surveyID) is None:
            surveyDocumentID = SurveyDocument.objects.create()
            surveyNumber = Survey.objects.create(SurveyDocumentID=surveyDocumentID)
        else:
            surveyNumber = Survey.objects.get(SurveyDocumentID=surveyID)

        questionNumber = SurveyQuestion.objects.create(
            SurveyID=surveyNumber,
            SurveyQuestionNumber=surveyQuestionNumber,
            SurveyQuestionSentence=surveyQuestionSentence,
        )

        for i in range(len(surveySelectionList)):
            SurveySelection.objects.create(
                SurveyQustionID=questionNumber,
                SurveySelectionNumber=i + 1,
                SurveySelectionSentence=surveySelectionList[i]
            )
