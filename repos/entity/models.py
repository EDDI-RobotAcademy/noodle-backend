from django.db import models

from account.entity.account import Account


class Repos(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"repo id: {self.id} -> reponame: {self.name} -> account: {self.account}"

    class Meta:
        db_table = "repos"
