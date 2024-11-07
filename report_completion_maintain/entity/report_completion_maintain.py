from django.db import models

from report_completion.entity.report_completion import ResultReportCompletion


class ResultReportCompletionMaintain(models.Model):
    id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    detail = models.TextField()
    completion = models.ForeignKey(ResultReportCompletion, on_delete=models.CASCADE, related_name="maintain")

    def __str__(self):
        return (f"ResultReportCompletionMaintainId: {self.id} -> ResultReportCompletionMaintainScore: {self.score}, "
                f"ResultReportCompletionMaintainDetail: {self.detail} on ResultReportCompletionId: {self.completion.id}")

    class Meta:
        db_table = "result_completion_maintain"
