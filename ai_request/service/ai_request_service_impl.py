from account.repository.account_repostiory_impl import AccountRepositoryImpl
from ai_request.repository.ai_request_repository_impl import AIRequestRepositoryImpl
from ai_request.service.ai_request_service import AIRequestService


class AIRequestServiceImpl(AIRequestService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__aiRequestRepository = AIRequestRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def aiRequestToFastAPI(self, userToken, accountId, command, data):
        try:
            account = self.__accountRepository.findAccountByAccountId(accountId)
        except Exception as e:
            print("aiRequestToFastAPI() 에서 account 찾는 중 에러 발생:", e)
            raise e

        try:
            return self.__aiRequestRepository.aiRequest(userToken, account.username, command, data)

        except Exception as e:
            print("Error creating Result Report:", e)
            raise e

