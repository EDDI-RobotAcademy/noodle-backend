from django.db import models

from subscription.entity.subscription_history import SubscriptionHistory
from subscription.entity.subscription_type_selections import SubscriptionTypeSelections


class SubscriptionType(models.Model):
    id = models.AutoField(primary_key=True)
    history_id = models.ForeignKey(SubscriptionHistory, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=SubscriptionTypeSelections.choices)

    class Meta:
        db_table = 'subscription_type'
