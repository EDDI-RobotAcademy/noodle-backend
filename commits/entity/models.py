from django.db import models

from branches.entity.models import Branches


class Commits(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    author = models.CharField(max_length=32)
    time = models.DateTimeField()
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)

    def __str__(self):
        return f"commits id: {self.id} -> commits author: {self.author} -> commits branch: {self.branch}\ncommit message: {self.message}"

    class Meta:
        db_table = "commits"
