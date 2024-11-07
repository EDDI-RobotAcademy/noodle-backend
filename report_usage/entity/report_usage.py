from django.db import models

from report.entity.report import ResultReport


class ResultReportUsage(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    report = models.ForeignKey(ResultReport, on_delete=models.CASCADE, related_name="report_usage")

    def __str__(self):
        return f"ResultReportUsageId: {self.id} -> ResultReportUsageContent: {self.content} on ResultReportId: {self.report.id}"

    class Meta:
        db_table = "report_usage"
