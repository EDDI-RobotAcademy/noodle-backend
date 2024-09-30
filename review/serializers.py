from rest_framework import serializers

from review.entity.review import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['reviewId', 'title', 'writer', 'content', 'image']
        read_only_fields = ['regDate', 'updDate']