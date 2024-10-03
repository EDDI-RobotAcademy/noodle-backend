from django.db import models

from backlog.entity.backlog import Backlog


class BacklogReview(models.Model):
    id = models.AutoField(primary_key=True)
    backlog = models.ForeignKey(Backlog, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()

    def __str(self):
        return f" Review for {self.backlog.title}: {self.review}"

    class Meta:
        db_table = 'backlog_review'