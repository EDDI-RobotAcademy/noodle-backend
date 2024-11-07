from report_completion_maintain.entity.report_completion_maintain import ResultReportCompletionMaintain
from report_completion_maintain.repository.report_completion_maintain_repository import \
    ResultReportCompletionMaintainRepository


class ResultReportCompletionMaintainRepositoryImpl(ResultReportCompletionMaintainRepository):
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

    def createResultReportCompletionMaintain(self, completion, score, detail):
        ResultReportCompletionMaintain.objects.create(completion=completion, score=score, detail=detail)

    def getResultReportCompletionMaintainByResultReportCompletion(self, completion):
        return ResultReportCompletionMaintain.objects.get(completion=completion)

    def delete(self, completionObj):
        ResultReportCompletionMaintain.objects.get(completion=completionObj).delete()
