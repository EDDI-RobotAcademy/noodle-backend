from django.db import models

from review.entity.point_choices import PointChoices
from review.entity.review_list import ReviewList


class SelectionReview(models.Model):
    id = models.AutoField(primary_key=True)
    listId = models.ForeignKey(ReviewList, on_delete=models.CASCADE, related_name='selection_review')
    writer = models.CharField(max_length=32, null=False)

    title = models.CharField(max_length=128, null=False)
    design = models.IntegerField(choices=[(int(choice[0]), choice[1]) for choice in PointChoices.choices()], )
    using = models.IntegerField(choices=[(int(choice[0]), choice[1]) for choice in PointChoices.choices()], )
    speed = models.IntegerField(choices=[(int(choice[0]), choice[1]) for choice in PointChoices.choices()], )
    quality = models.IntegerField(choices=[(int(choice[0]), choice[1]) for choice in PointChoices.choices()], )
    feedback = models.TextField()

    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'selection_review'
