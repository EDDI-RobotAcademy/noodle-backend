from django.db import models


class MeetingRecordingSummary(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    writer = models.CharField(max_length=32)
    content = models.TextField()
    regDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"MeetingRecordingSummary: id: {self.id}, title: {self.title}, writer: {self.writer}\n"
                f"content: {self.content}, regDate: {self.regDate}")

    class Meta:
        db_table = "meeting_recording_summary"
