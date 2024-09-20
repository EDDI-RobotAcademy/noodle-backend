from django.db import models

from survey.entity.survey_document import SurveyDocument


class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    SurveyDocumentID = models.ForeignKey(SurveyDocument, on_delete=models.CASCADE)

    def __str__(self):
        return f"id: {self.id}, documentID: {self.SurveyDocumentID.id}"

    class Meta:
        db_table = 'survey'
        app_label = 'survey'
