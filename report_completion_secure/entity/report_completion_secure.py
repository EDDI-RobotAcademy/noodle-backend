from django.db import models

from report_completion.entity.report_completion import ResultReportCompletion


class ResultReportCompletionSecure(models.Model):
    id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    detail = models.TextField()
    completion = models.ForeignKey(ResultReportCompletion, on_delete=models.CASCADE, related_name="secure")

    def __str__(self):
        return (f"ResultReportCompletionSecureId: {self.id} -> ResultReportCompletionSecureScore: {self.score}, "
                f"ResultReportCompletionSecureDetail: {self.detail} on ResultReportCompletionId: {self.completion.id}")

    class Meta:
        db_table = "report_completion_secure"
