from report_completion_total.entity.report_completion_total import ResultReportCompletionTotal
from report_completion_total.repository.report_completion_total_repository import ResultReportCompletionTotalRepository

class ResultReportCompletionTotalRepositoryImpl(ResultReportCompletionTotalRepository):
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

    def createResultReportCompletionTotal(self, completion, score, detail):
        ResultReportCompletionTotal.objects.create(completion=completion, score=score, detail=detail)

    def getResultReportCompletionTotalByResultReportCompletion(self, completion):
        return ResultReportCompletionTotal.objects.get(completion=completion)
