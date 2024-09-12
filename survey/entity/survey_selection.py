from django.db import models

from survey.entity.survey_question import SurveyQuestion


class SurveySelection(models.Model):
    id = models.AutoField(primary_key=True)
    SurveyQuestionID = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)

    class Meta:
        db_table = "survey_selection"
        app_label = "survey"
