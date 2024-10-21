from rest_framework import viewsets, status
from rest_framework.response import Response

from account.service.account_service_impl import AccountServiceImpl
from github_oauth.service.redis_service_impl import RedisServiceImpl


class AccountView(viewsets.ViewSet):
    accountService = AccountServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def checkUserNameDuplication(self, request):
        print("checkUserNameDuplication()")

        try:
            username = request.data.get('username')
            print(f"username: {username}")
            isDuplicate = self.accountService.checkUsernameDuplication(username)

            return Response({'isDuplicate': isDuplicate, 'message': 'Username이 이미 존재' \
                             if isDuplicate else 'Username 사용 가능'}, status=status.HTTP_200_OK)
        except Exception as e:
            print("닉네임 중복 체크 중 에러 발생", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def getUserNameByUserToken(self, request):
        print("getUserName")

        try:
            userToken = request.data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)
            account = self.accountService.findAccountByAccountId(accountId)

            return Response({"username": account.username}, status=status.HTTP_200_OK)

        except Exception as e:
            print("유저 토큰으로 닉네임 찾는 중 에러 발생", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)