from rest_framework import viewsets, status
from rest_framework.response import Response

from account.service.account_service_impl import AccountServiceImpl


class AccountView(viewsets.ViewSet):
    accountService = AccountServiceImpl.getInstance()

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