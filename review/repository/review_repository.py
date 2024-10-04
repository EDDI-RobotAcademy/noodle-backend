from abc import ABC, abstractmethod

class ReviewRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createReview(self, title, writer, content, image):
        pass

    @abstractmethod
    def createReviewWithoutImage(self, title, writer, content):
        pass