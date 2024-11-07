from rest_framework import viewsets, status
from rest_framework.response import Response

from account.service.account_service_impl import AccountServiceImpl
from github_oauth.service.redis_service_impl import RedisServiceImpl
from subscription.service.subscription_service_impl import SubscriptionServiceImpl


class SubscriptionView(viewsets.ViewSet):
    redisService = RedisServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()
    subscriptionService = SubscriptionServiceImpl.getInstance()

    def registerSubscription(self, request):
        try:
            userToken = request.data.get('userToken')
            ticketType = request.data.get('ticket')
            paymentID = request.data.get('paymentID')

            if not userToken or not ticketType or not paymentID:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            userId = self.redisService.getValueByKey(userToken)
            account = self.accountService.findAccountByAccountId(userId)

            history = self.subscriptionService.registerSubscriptionHistory(account)
            self.redisService.setSubscriptionRemainingTime(userId, ticketType)
            self.subscriptionService.registerSubscriptionTicketType(history, ticketType)
            self.subscriptionService.registerSubscriptionPaymentInformation(history, paymentID)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def checkSubscription(self, request):
        try:
            userToken = request.data.get('userToken')
            if not userToken:
                return Response({"type": 0}, status=status.HTTP_200_OK)
            userId = self.redisService.getValueByKey(userToken)
            type = self.redisService.checkSubscription(userId)
            return Response({"type": type}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
