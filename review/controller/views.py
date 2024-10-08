from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.service.account_service_impl import AccountServiceImpl
from github_oauth.service.redis_service_impl import RedisServiceImpl
from review.entity.writing_review import WritingReview
from review.serializers import ReviewSerializer
from review.service.review_service_impl import ReviewServiceImpl


# Create your views here.

class ReviewView(viewsets.ViewSet):
    queryset = WritingReview.objects.all()

    reviewService = ReviewServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()

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
        return Response({'list': reviewList}, status=status.HTTP_200_OK)

    def registerNewWritingReview(self, request):
        try:
            data = request.data

            # image = request.FILES.get('reviewImage')
            title = data.get('title')
            userToken = data.get('userToken')
            content = data.get('content')

            accountId = self.redisService.getValueByKey(userToken)
            writer = self.accountService.findAccountByAccountId(accountId)

            if not all([title, writer.username, content]):
                return Response({'error': '내용을 채워주세요!'},
                                status=status.HTTP_400_BAD_REQUEST)

            # self.reviewService.createReview(title, writer, content, image)
            reviewList = self.reviewService.createNewWritingReviewListID()
            self.reviewService.registerNewWritingReview(title, writer.username, content, reviewList)

            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('리뷰 등록 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def readReview(self, request, pk=None):
        review = self.reviewService.readReview(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
