from django.db import models

from account.entity.account import Account


class SubscriptionHistory(models.Model):
    id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    regDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'subscription_history'
