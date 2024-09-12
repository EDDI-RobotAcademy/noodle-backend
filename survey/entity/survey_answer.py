from django.db import models

from survey.entity.survey_question import SurveyQuestion
from survey.entity.survey_selection import SurveySelection


class SurveyAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    SurveyQuestionID = models.ForeignKey(SurveyQuestion, models.CASCADE)
    SurveySelectionID = models.ForeignKey(SurveySelection, models.CASCADE)

    class Meta:
        db_table = "survey_answer"
        app_label = "survey"
