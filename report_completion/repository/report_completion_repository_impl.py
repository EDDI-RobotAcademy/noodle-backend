from report_completion.entity.report_completion import ResultReportCompletion
from report_completion.repository.report_completion_repository import ResultReportCompletionRepository


class ResultReportCompletionRepositoryImpl(ResultReportCompletionRepository):
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

    def getResultRepositoryCompletionByResultReport(self, report):
        return ResultReportCompletion.objects.get(report=report)

    def createResultReportCompletion(self, report):
        ResultReportCompletion.objects.create(report=report)
