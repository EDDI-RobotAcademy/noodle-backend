from abc import ABC, abstractmethod


class ReviewService(ABC):
    @abstractmethod
    def reviewList(self, pageCount, countsPerPage):
        pass

    @abstractmethod
    def createReview(self, title, writer, content, image):
        pass

    @abstractmethod
    def registerNewWritingReview(self, title, writer, content, reviewList):
        pass

    @abstractmethod
    def readReview(self, reviewId):
        pass

    @abstractmethod
    def getEntireReviewListCount(self):
        pass

    @abstractmethod
    def createNewReviewListID(self):
        pass
