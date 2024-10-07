from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from backlog_review.service.backlog_review_service_impl import BacklogReviewServiceImpl


class BacklogReviewView(viewsets.ViewSet):
    backlogReviewService = BacklogReviewServiceImpl.getInstance()

    def createBacklogReview(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        review = data.get('review')

        createdBacklogReview = self.backlogReviewService.createBacklogReview(backlogId, review).review

        return Response(createdBacklogReview, status=status.HTTP_200_OK)