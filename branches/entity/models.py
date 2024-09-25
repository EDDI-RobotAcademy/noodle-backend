from django.db import models

from repos.entity.models import Repos


class Branches(models.Model):
    id = models.AutoField(primary_key=True)
    branchname = models.CharField(max_length=64)
    repos = models.ForeignKey(Repos, on_delete=models.CASCADE)

    def __str__(self):
        return f"branch id: {self.id} -> branch name: {self.branchname} -> repos: {self.repos}"

    class Meta:
        db_table = "branches"
