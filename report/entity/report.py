from django.db import models


class ResultReport(models.Model):
    id = models.AutoField(primary_key=True)
    creator = models.CharField(max_length=128)
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result Report {self.id}"

    class Meta:
        db_table = "result_report"
