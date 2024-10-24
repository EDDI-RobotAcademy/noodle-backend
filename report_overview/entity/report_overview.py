from django.db import models

from report.entity.report import ResultReport


class ResultReportOverview(models.Model):
    id = models.AutoField(primary_key=True)
    overview = models.TextField()
    report = models.ForeignKey(ResultReport, on_delete=models.CASCADE, related_name="overview")

    def __str__(self):
        return f"Report {self.report.id} Overview: {self.overview}"

    class Meta:
        db_table = "report_overview"
