from django.db import models

from backlog.entity.backlog import Backlog


class BacklogTodo(models.Model):
    id = models.AutoField(primary_key=True)
    backlog = models.ForeignKey(Backlog, on_delete=models.CASCADE, related_name='todos')
    todo = models.CharField(max_length=500)

    def __str__(self):
        return f"Todo for {self.backlog.title}: {self.todo}"

    class Meta:
        db_table = 'backlog_todo'