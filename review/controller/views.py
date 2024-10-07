from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from review.entity.writing_review import WritingReview
from review.serializers import ReviewSerializer
from review.service.review_service_impl import ReviewServiceImpl


# Create your views here.

class ReviewView(viewsets.ViewSet):
    queryset = WritingReview.objects.all()

    reviewService = ReviewServiceImpl.getInstance()

    def entireReviewListCount(self, request):
        try:
            count = self.reviewService.getEntireReviewListCount()
            return Response({'count': count}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def reviewList(self, request):
        pageCount = request.data.get('pagination')
        countsPerPage = request.data.get('perPage')
        print(pageCount, countsPerPage)

        reviewList = self.reviewService.reviewList(pageCount, countsPerPage)
        return Response(reviewList, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            data = request.data

            # image = request.FILES.get('reviewImage')
            title = data.get('title')
            writer = data.get('writer')
            content = data.get('content')

            if not all([title, writer, content]):
                return Response({'error': '내용을 채워주세요!'},
                                status=status.HTTP_400_BAD_REQUEST)

            # self.reviewService.createReview(title, writer, content, image)
            self.reviewService.createReviewWithoutImage(title, writer, content)

            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('리뷰 등록 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def readReview(self, request, pk=None):
        review = self.reviewService.readReview(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
