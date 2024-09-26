from account.entity.account import Account
from account.entity.account_role_type import AccountRoleType
from account.repository.account_repository import AccountRepository


class AccountRepositoryImpl(AccountRepository):
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

    def findAccountByUsername(self, username):
        try:
            account = Account.objects.get(username=username)
            return account
        except Account.DoesNotExist:
            print(f"username으로 account 찾을 수 없음: {username}")
            return None
        except Exception as e:
            print(f"username 중복 검사 중 에러 발생: {e}")
            return None

    def findAccountByAccountId(self, account_id):
        account = Account.objects.get(id=account_id)
        return account

    def saveAccountByUsername(self, nickname):
        roleType = AccountRoleType.objects.get(roleType='NORMAL')
        account = Account.objects.get(username=nickname)
        if not account:
            account = Account.objects.create(username=nickname, roleType=roleType)
        else:
            print("user is already registered")
        return account
