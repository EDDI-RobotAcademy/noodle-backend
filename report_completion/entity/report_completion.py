from django.db import models

from report.entity.report import ResultReport


class ResultReportCompletion(models.Model):
    id = models.AutoField(primary_key=True)
    report = models.ForeignKey(ResultReport, on_delete=models.CASCADE, related_name="completion")

    def __str__(self):
        return f"ResultReportCompletionId: {self.id} on ResultReportId: {self.report.id}"

    class Meta:
        db_table = "report_completion"
