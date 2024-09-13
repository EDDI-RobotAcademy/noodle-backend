from survey.entity.survey_answer import SurveyAnswer
from survey.entity.survey_question import SurveyQuestion
from survey.entity.survey_selection import SurveySelection
from survey.repository.survey_repository import SurveyRepository


class SurveyRepositoryImpl(SurveyRepository):
    def save(self, surveyNumber, surveyQuestionNumber, surveySelectionNumber):
        surveyQuestion = SurveyQuestion.objects.get(SurveyID=surveyNumber)
        surveyQuestionNumber = surveyQuestion.objects.get(SurveyQuestionNumber=surveyQuestionNumber)
        surveySelection = SurveySelection.objects.get(SurveyQuestionID=surveyQuestionNumber.id)
        surveySelectionNumber = surveySelection.objects.get(SurveySelectionNumber=surveySelectionNumber)

        SurveyAnswer.objects.create(
            SurveyQuestionID=surveyQuestionNumber.id,
            SurveySelectionID=surveySelectionNumber.id
        )