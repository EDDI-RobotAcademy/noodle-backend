from django.db import models


class ResultReportTeam(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"ResultReportTeam: ResultReportTeam {self.id}"

    class Meta:
        db_table = "report_team"
