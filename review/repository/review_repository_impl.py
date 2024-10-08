import os

from noodle_project import settings
from review.entity.review_list import ReviewList
from review.entity.review_type import ReviewType
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

    def registerNewWritingReview(self, title, writer, content, reviewList):
        review = WritingReview(title=title, writer=writer, content=content, listId=reviewList)
        review.save()

        return review

    def findById(self, reviewId):
        return WritingReview.objects.get(reviewId=reviewId)

    def selectionReviewSlicedList(self, startIndex, endIndex):
        slicedIdListForSelectionReview = ReviewList.objects.filter(id__range=(startIndex, endIndex))
        print(f'slicedIdListForSelectionReview {slicedIdListForSelectionReview}')

        slicedSelectionReview = []
        for item in slicedIdListForSelectionReview:
            try:
                slicedSelectionReview.append(SelectionReview.objects.get(listId=item.id))
            except SelectionReview.DoesNotExist:
                continue

        print(f'slicedSelectionReview {slicedSelectionReview}')
        return slicedSelectionReview

    def writingReviewSlicedList(self, startIndex, endIndex):
        slicedIdListForWritingReview = ReviewList.objects.filter(id__range=(startIndex, endIndex))
        print(f'slicedIdListForWritingReview {slicedIdListForWritingReview}')

        slicedWritingReview = []
        for item in slicedIdListForWritingReview:
            try:
                slicedWritingReview.append(WritingReview.objects.get(listId=item.id))
            except WritingReview.DoesNotExist:
                continue

        print(f'slicedWritingReview {slicedWritingReview}')
        return slicedWritingReview

    def getEntireReviewListCount(self):
        print('repository-> getEntireReviewListCount()')
        return ReviewList.objects.count()

    def createNewReviewListID(self):
        print('repository -> createNewReviewListID()')
        return ReviewList.objects.create()
