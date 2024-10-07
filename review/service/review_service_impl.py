from review.repository.review_repository_impl import ReviewRepositoryImpl
from review.service.review_service import ReviewService


class ReviewServiceImpl(ReviewService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__reviewRepository = ReviewRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def reviewList(self, pageCount, countsPerPage):
        startIndex = (pageCount - 1) * countsPerPage
        endIndex = pageCount * countsPerPage

        selectionReview = self.__reviewRepository.selectionReviewSlicedList(startIndex, endIndex)
        writingReview = self.__reviewRepository.writingReviewSlicedList(startIndex, endIndex)

        reviewList = self.__reviewRepository.joinList(selectionReview, writingReview)
        print('joinedReviewList', reviewList)
        return reviewList

    def createReview(self, title, writer, content, image):
        return self.__reviewRepository.createReview(title, writer, content, image)

    def createReviewWithoutImage(self, title, writer, content):
        return self.__reviewRepository.createReviewWithoutImage(title, writer, content)

    def readReview(self, reviewId):
        return self.__reviewRepository.findById(reviewId)
