from rest_framework import serializers

from review.entity.writing_review import WritingReview

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = WritingReview
        fields = ['reviewId', 'title', 'writer', 'content', 'image', 'listId']
        read_only_fields = ['regDate', 'updDate']