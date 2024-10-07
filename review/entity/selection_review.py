from django.db import models

from review.entity.point_choices import PointChoices
from review.entity.review_list import ReviewList


class SelectionReview(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False)
    listId = models.ForeignKey(ReviewList, on_delete=models.CASCADE, related_name='selection_review')
    using = models.IntegerField(choices=[(int(choice[0]), choice[1]) for choice in PointChoices.choices()],
        default=int(PointChoices.ZERO.value))
    speed = models.IntegerField(choices=[(int(choice[0]), choice[1]) for choice in PointChoices.choices()],
        default=int(PointChoices.ZERO.value))
    design = models.IntegerField(choices=[(int(choice[0]), choice[1]) for choice in PointChoices.choices()],
        default=int(PointChoices.ZERO.value))
    quality = models.IntegerField(choices=[(int(choice[0]), choice[1]) for choice in PointChoices.choices()],
        default=int(PointChoices.ZERO.value))
    feedback = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'review_selection'