import os

from noodle_project import settings
from review.entity.selection_review import SelectionReview
from review.entity.writing_review import WritingReview
from review.repository.review_repository import ReviewRepository
from itertools import chain
from operator import attrgetter

class ReviewRepositoryImpl(ReviewRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def selectionList(self):
        return SelectionReview.objects.all()

    def writingList(self):
        return WritingReview.objects.all()

    def joinList(self, selectionReview, writingReview):
        return sorted(chain(selectionReview, writingReview),
                      key=attrgetter('listId'))

    def createReview(self, title, writer, content, image):
        uploadDirectory = os.path.join(
            settings.BASE_DIR,
            '../../../../../noodle-frontend/src/assets/images/uploadImages'
        )
        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)

        imagePath = os.path.join(uploadDirectory, image.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

            destination.flush()
            os.fsync(destination.fileno())

        review = WritingReview(title=title, writer=writer, content=content, image=image)
        review.save()

        return review


    def createReviewWithoutImage(self, title, writer, content):
        review = WritingReview(title=title, writer=writer, content=content)
        review.save()

        return review

    def findById(self, reviewId):
        return WritingReview.objects.get(reviewId=reviewId)



