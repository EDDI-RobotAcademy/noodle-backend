from django.db import models

from report_feature.entity.report_feature import ResultReportFeature


class ResultReportFeatureContent(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    feature = models.ForeignKey(ResultReportFeature, on_delete=models.CASCADE, related_name="feature_content")

    def __str__(self):
        return f"ResultReportFeatureContentId: {self.id}"

    class Meta:
        db_table = "report_feature_content"
