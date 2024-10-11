from django.db import models

from report.entity.report import ResultReport


class ResultReportTeam(models.Model):
    id = models.AutoField(primary_key=True)
    report = models.ForeignKey(ResultReport, on_delete=models.CASCADE, related_name="team")

    def __str__(self):
        return f"ResultReportTeam: ResultReportTeam {self.id}"

    class Meta:
        db_table = "report_team"
