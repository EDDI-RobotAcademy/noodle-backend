import os

from noodle_project import settings
from review.entity.review import Review
from review.repository.review_repository import ReviewRepository


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

    def list(self):
        return Review.objects.all().order_by('-regDate')

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

        review = Review(title=title, writer=writer, content=content, image=image)
        review.save()

        return review


    def createReviewWithoutImage(self, title, writer, content):
        review = Review(title=title, writer=writer, content=content)
        review.save()

        return review

    def findById(self, reviewId):
        return Review.objects.get(id)



