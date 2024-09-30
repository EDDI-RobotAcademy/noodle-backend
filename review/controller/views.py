from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from review.entity.review import Review
from review.serializers import ReviewSerializer


# Create your views here.

class ReviewView(viewsets.ViewSet):
    queryset = Review.objects.all()

    reviewService = ReviewServiceImpl.getInstance()

    def list(self, request):
        reviewList = self.reviewService.list()
        serializer = ReviewSerializer(reviewList, many=True)
        return Response(serializer.data)