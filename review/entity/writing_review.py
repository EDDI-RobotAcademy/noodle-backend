from django.db import models

from review.entity.review_list import ReviewList


class WritingReview(models.Model):
    reviewId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False)
    writer = models.CharField(max_length=32, null=False)
    content = models.TextField()
    image = models.CharField(max_length=100, null=True)

    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)
    listId = models.ForeignKey(ReviewList, on_delete=models.CASCADE, related_name='writing_review')
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'review'