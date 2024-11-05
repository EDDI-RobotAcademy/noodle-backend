from report_completion_secure.entity.report_completion_secure import ResultReportCompletionSecure
from report_completion_secure.repository.report_completion_secure_repository import \
    ResultReportCompletionSecureRepository


class ResultReportCompletionSecureRepositoryImpl(ResultReportCompletionSecureRepository):
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

    def createResultReportCompletionSecure(self, completion, score, detail):
        ResultReportCompletionSecure.objects.create(completion=completion, score=score, detail=detail)

    def getResultReportCompletionSecureByResultReportCompletion(self, completion):
        return ResultReportCompletionSecure.objects.get(completion=completion)

    def delete(self, completionObj):
        ResultReportCompletionSecure.objects.get(completion=completionObj).delete()
