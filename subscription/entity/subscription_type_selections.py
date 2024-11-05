from django.db import models


class SubscriptionTypeSelections(models.TextChoices):
    JUNIOR = 'JUNIOR'
    SENIOR = 'SENIOR'
    LEADER = 'LEADER'
