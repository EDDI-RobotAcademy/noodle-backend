from django.db import models

from report.entity.report import ResultReport


class ResultReportImprovement(models.Model):
    id = models.AutoField(primary_key=True)
    report = models.ForeignKey(ResultReport, on_delete=models.CASCADE, related_name="improvement")

    def __str__(self):
        return f"ResultReportImprovementId: {self.id} on ResultReportId: {self.report.id}"

    class Meta:
        db_table = "report_improvement"
