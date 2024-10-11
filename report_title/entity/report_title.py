from django.db import models

from report.entity.report import ResultReport


class ResultReportTitle(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    report = models.ForeignKey(ResultReport, on_delete=models.CASCADE, related_name="report-title")

    def __str__(self):
        return f"Result Report Id: {self.report.id} -> Result Report Title: {self.title}"

    class Meta:
        db_table = "report_title"
