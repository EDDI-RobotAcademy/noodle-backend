from django.db import models

from report.entity.report import ResultReport


class ResultReportSkillSet(models.Model):
    id = models.AutoField(primary_key=True)
    report = models.ForeignKey(ResultReport, on_delete=models.CASCADE, related_name="skill_set")

    def __str__(self):
        return f"ResultReportSkillSetId: {self.id}"

    class Meta:
        db_table = "report_skill_set"
