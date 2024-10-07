from abc import ABC, abstractmethod


class ReviewService(ABC):
    @abstractmethod
    def reviewList(self, pageCount, countsPerPage):
        pass

    @abstractmethod
    def createReview(self, title, writer, content, image):
        pass

    @abstractmethod
    def createReviewWithoutImage(self, title, writer, content):
        pass

    @abstractmethod
    def readReview(self, reviewId):
        pass

    @abstractmethod
    def getEntireReviewListCount(self):
        pass
