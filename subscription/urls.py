from django.urls import path, include
from rest_framework.routers import DefaultRouter

from subscription.controller.views import SubscriptionView

router = DefaultRouter()
router.register(r'subscription', SubscriptionView, basename='subscription')

urlpatterns = [
    path('', include(router.urls)),
    path('register', SubscriptionView.as_view({'post': 'registerSubscription'}),
         name='registering-subscription'),
    path('check', SubscriptionView.as_view({'post': 'checkSubscription'}), name='subscription-check')
]
