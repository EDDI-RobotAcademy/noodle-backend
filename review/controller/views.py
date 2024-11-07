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

        reviewList = self.reviewService.reviewList(pageCount, countsPerPage)
        return Response({'list': reviewList}, status=status.HTTP_200_OK)

    def registerNewWritingReview(self, request):
        try:
            data = request.data

            # image = request.FILES.get('reviewImage')
            title = data.get('title')
            userToken = data.get('userToken')
            content = data.get('content')

            if userToken == 'anonymous':
                username = '익명'
            else:
                accountId = self.redisService.getValueByKey(userToken)
                writer = self.accountService.findAccountByAccountId(accountId)
                username = writer.username

            # self.reviewService.createReview(title, writer, content, image)
            reviewList = self.reviewService.createNewWritingReviewListID()
            self.reviewService.registerNewWritingReview(title, username, content, reviewList)

            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('리뷰 등록 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def modifyReview(self, request):
        try:
            data = request.data

            id = data.get('reviewID')
            content = data.get('content')

            userToken = request.data.get('userToken')
            if userToken == None:
                print('userToken is None')
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            userid = self.redisService.getValueByKey(userToken)
            userObj = self.accountService.findAccountByAccountId(userid)
            name = userObj.username
            if name == None:
                name = 'anonymous'
            if request.data.get('writer') != name:
                print('not matching')
                return Response(status=status.HTTP_401_UNAUTHORIZED)

            review, type = self.reviewService.findReviewByReviewID(id)
            if type == 'SELECTION':
                ratingList = request.data.get('ratingList')
                self.reviewService.modifySelectionReview(review, ratingList, content)
                return Response({'response': True}, status=status.HTTP_200_OK)
            else:
                title = data.get('title')
                self.reviewService.modifyWritingReview(review, title, content)
                return Response({'response': True}, status=status.HTTP_200_OK)
        except Exception as e:
            print('리뷰 수정 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def registerNewSelectionReview(self, request):
        try:
            userToken = request.data.get('userToken')
            ratingList = request.data.get('ratingList')
            content = request.data.get('content')

            if userToken == 'anonymous':
                username = '익명'
            else:
                accountId = self.redisService.getValueByKey(userToken)
                writer = self.accountService.findAccountByAccountId(accountId)
                username = writer.username

            reviewList = self.reviewService.createNewSelectionReviewListId()
            self.reviewService.registerNewSelectionReview('님의 평점 리뷰', username, ratingList, content, reviewList)

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print('리뷰 등록 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def readReview(self, request):
        try:
            reviewID = request.data.get("reviewID")
            response = self.reviewService.readReview(reviewID)

            return Response(response, status=status.HTTP_200_OK)


        except Exception as e:
            print("error occurred while reading review!", e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def deleteReview(self, request):
        try:
            userToken = request.data.get('userToken')
            if userToken == None:
                print('userToken is None')
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            id = self.redisService.getValueByKey(userToken)
            userObj = self.accountService.findAccountByAccountId(id)
            name = userObj.username
            if name == None:
                name = 'anonymous'
            if request.data.get('writer') != name:
                print('not matching')
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            reviewID = request.data.get("reviewID")
            self.reviewService.deleteReivew(reviewID)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print("error occurred while deleting review!", e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
