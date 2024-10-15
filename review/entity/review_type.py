from django.db import models

class ReviewType(models.TextChoices):
    WRITING = 'WRITING'
    SELECTION = 'SELECTION'