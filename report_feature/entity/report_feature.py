from django.db import models

from report.entity.report import ResultReport


class ResultReportFeature(models.Model):
    id = models.AutoField(primary_key=True)
    report = models.ForeignKey(ResultReport, on_delete=models.CASCADE, related_name='feature')

    def __str__(self):
        return f"ResultReportFeatureId: {self.id} on ResultReportId: {self.report.id}"

    class Meta:
        db_table = "report_feature"
