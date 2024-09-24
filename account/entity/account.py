from django.db import models
from account_role_type import AccountRoleType


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=64)
    roleType = models.ForeignKey(AccountRoleType, on_delete=models.CASCADE)

    def __str__(self):
        return f"Account: {self.id}, userName: {self.userName}, roleType: {self.roleType}"

    class Meta:
        db_table = 'account'
        app_label = 'account'