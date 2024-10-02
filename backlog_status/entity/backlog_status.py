from django.db import models

from backlog.entity.backlog import Backlog
from backlog_status.entity.backlog_status_type import BacklogStatusType


class BacklogStatus(models.Model):
    id = models.AutoField(primary_key=True)
    backlog = models.ForeignKey(Backlog, on_delete=models.CASCADE, related_name='statuses')
    status = models.IntegerField(
        choices=BacklogStatusType.choices(),
        default=BacklogStatusType.BACKLOG.value
    )