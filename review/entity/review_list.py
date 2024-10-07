from django.db import models

from review.entity.review_type import ReviewType


class ReviewList(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=64, choices=ReviewType.choices, default=ReviewType.SELECTION)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'review_list'