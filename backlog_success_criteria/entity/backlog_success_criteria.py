from django.db import models

from backlog.entity.backlog import Backlog


class BacklogSuccessCriteria(models.Model):
    id = models.AutoField(primary_key=True)
    backlog = models.ForeignKey(Backlog, on_delete=models.CASCADE, related_name="success_criteria")
    successCriteria = models.TextField()

    def __str__(self):
        return f"Criteria for {self.backlog.title}: {self.success_criteria}"

    class Meta:
        db_table = 'backlog_success_criteria'