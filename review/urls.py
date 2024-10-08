from django.urls import path, include
from rest_framework.routers import DefaultRouter

from review.controller.views import ReviewView

router = DefaultRouter()
router.register(r'review', ReviewView)

urlpatterns = [
    path('', include(router.urls)),
    path('list', ReviewView.as_view({'post': 'reviewList'}), name='review-list'),
    path('register/writingReview', ReviewView.as_view({'post': 'registerNewWritingReview'}), name='writing-review-register'),
    path('register/selectionReview', ReviewView.as_view({'post':'registerNewSelectionReview'}, name='selection-review-register')),
    path('read/<int:pk>', ReviewView.as_view({'get': 'read'}), name='review-read'),
    path('entire-count', ReviewView.as_view({'post': 'entireReviewListCount'}), name='review-list-entire-count'),
]
