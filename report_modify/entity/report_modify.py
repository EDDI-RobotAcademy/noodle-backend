from django.db import models

from report.entity.report import ResultReport


class ResultReportModify(models.Model):
    id = models.AutoField(primary_key=True)
    modifier = models.CharField(max_length=128)
    modifyDate = models.DateTimeField(auto_now=True)
    report = models.ForeignKey(ResultReport, on_delete=models.CASCADE, related_name="modify")

    def __str__(self):
        return f"Result Report Id: {self.report.id} -> Modifier: {self.modifier}, ModifyDate: {self.modifyDate}"

    class Meta:
        db_table = "result_report_modify"
        