from django.db import models

from backlog.entity.backlog import Backlog


class BacklogIssue(models.Model):
    id = models.AutoField(primary_key=True)
    backlog = models.ForeignKey(Backlog, on_delete=models.CASCADE, related_name='issues')
    issue = models.CharField(max_length=500)

    def __str__(self):
        return f"Issue for {self.backlog.title}: {self.issue}"

    class Meta:
        db_table = 'backlog_issue'