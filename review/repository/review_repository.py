from abc import ABC, abstractmethod


class ReviewRepository(ABC):
    @abstractmethod
    def selectionList(self):
        pass

    @abstractmethod
    def writingList(self):
        pass

    @abstractmethod
    def joinList(self, selectionReview, writingReview):
        pass

    @abstractmethod
    def createReview(self, title, writer, content, image):
        pass

    @abstractmethod
    def registerNewWritingReview(self, title, writer, content, reviewList):
        pass

    @abstractmethod
    def findById(self, reviewId):
        pass

    @abstractmethod
    def selectionReviewSlicedList(self, startIndex, endIndex):
        pass

    @abstractmethod
    def writingReviewSlicedList(self, startIndex, endIndex):
        pass

    @abstractmethod
    def getEntireReviewListCount(self):
        pass

    @abstractmethod
    def createNewReviewListID(self):
        pass
