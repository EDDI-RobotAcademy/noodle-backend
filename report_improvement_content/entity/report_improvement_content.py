from django.db import models

from report_improvement.entity.report_improvement import ResultReportImprovement


class ResultReportImprovementContent(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    improvement = models.ForeignKey(ResultReportImprovement, on_delete=models.CASCADE, related_name="improvement_content")

    def __str__(self):
        return (f"ResultReportImprovementContentId: {self.id} -> ResultReportImprovementContent: {self.content} "
                f"on ResultReportImprovementId: {self.improvement.id}")

    class Meta:
        db_table = "report_improvement_content"
