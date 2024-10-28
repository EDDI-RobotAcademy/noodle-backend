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
    def registerNewSelectionReview(self, title, writer, ratingList, content, reviewList):
        pass

    @abstractmethod
    def readReview(self, reviewId):
        pass

    @abstractmethod
    def getEntireReviewListCount(self):
        pass

    @abstractmethod
    def createNewWritingReviewListID(self):
        pass

    @abstractmethod
    def createNewSelectionReviewListId(self):
        pass

    @abstractmethod
    def findReviewByReviewID(self, id):
        pass

    @abstractmethod
    def modifySelectionReview(self, review, ratingList, content):
        pass

    @abstractmethod
    def modifyWritingReview(self, review, title, content):
        pass

    @abstractmethod
    def deleteReivew(self, reviewID):
        pass
