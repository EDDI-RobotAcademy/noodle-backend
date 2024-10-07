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
    def createReviewWithoutImage(self, title, writer, content):
        pass

    @abstractmethod
    def findById(self, reviewId):
        pass
