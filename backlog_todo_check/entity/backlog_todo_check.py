from django.db import models

from backlog_todo.entity.backlog_todo import BacklogTodo


class BacklogTodoCheck(models.Model):
    id = models.AutoField(primary_key=True)
    backlogTodo = models.ForeignKey(BacklogTodo, on_delete=models.CASCADE, related_name='checks')
    isChecked = models.BooleanField(default=False)

    def __str__(self):
        return f"Todo Check for {self.backlogTodo.todo}: {'Checked' if self.isChecked else 'Unchecked'}"

    class Meta:
        db_table = 'backlog_todo_check'