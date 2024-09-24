from django.db import models

from survey.entity.survey_question import SurveyQuestion


class SurveySelection(models.Model):
    id = models.AutoField(primary_key=True)
    SurveyQuestionID = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    SurveySelectionNumber = models.IntegerField(default=0)
    SurveySelectionSentence = models.CharField(max_length=100, default=None)

    class Meta:
        db_table = "survey_selection"
        app_label = "survey"
