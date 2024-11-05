from django.db import models

from subscription.entity.subscription_history import SubscriptionHistory


class SubscriptionPaymentInformation(models.Model):
    id = models.AutoField(primary_key=True)
    history_id = models.ForeignKey(SubscriptionHistory, on_delete=models.CASCADE)
    paymentID = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'subscription_payment_information'
