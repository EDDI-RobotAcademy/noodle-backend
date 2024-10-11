import datetime

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
        count = self.__reviewRepository.getEntireReviewListCount()
        endIndex = count - ((pageCount - 1) * countsPerPage)
        startIndex = count - (pageCount * countsPerPage)
        if startIndex < 0:
            startIndex = 0

        selectionReview = self.__reviewRepository.selectionReviewSlicedList(startIndex, endIndex)
        writingReview = self.__reviewRepository.writingReviewSlicedList(startIndex, endIndex)

        reviewList = self.__reviewRepository.joinList(selectionReview, writingReview)

        # TODO: sorting로직이 필요한지 검증 필요.
        # reviewList.sort()
        reversedReviewList = reversed(reviewList)
        parsedReviewList = [
            {
                'id': review.listId.id,
                'title': review.title,
                'writer': review.writer,
                'regDate': review.regDate.astimezone(datetime.timezone(datetime.timedelta(hours=9))).strftime(
                    '%Y-%m-%d %H:%M:%S')
            }
            for review in reversedReviewList
        ]

        return parsedReviewList

    def createReview(self, title, writer, content, image):
        return self.__reviewRepository.createReview(title, writer, content, image)

    def registerNewWritingReview(self, title, writer, content, reviewList):
        return self.__reviewRepository.registerNewWritingReview(title, writer, content, reviewList)

    def registerNewSelectionReview(self, title, writer, ratingList, content, reviewList):
        return self.__reviewRepository.registerNewSelectionReview(title, writer, ratingList, content, reviewList)

    def readReview(self, reviewId):

        return self.__reviewRepository.findReviewById(reviewId)

    def getEntireReviewListCount(self):
        return self.__reviewRepository.getEntireReviewListCount()

    def createNewWritingReviewListID(self):
        return self.__reviewRepository.createNewWritingReviewListID()

    def createNewSelectionReviewListId(self):
        return self.__reviewRepository.createNewSelectionReviewListId()
