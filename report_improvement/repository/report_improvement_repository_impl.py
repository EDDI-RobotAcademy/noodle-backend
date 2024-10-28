from report_improvement.entity.report_improvement import ResultReportImprovement
from report_improvement.repository.report_improvement_repository import ResultReportImprovementRepository

class ResultReportImprovementRepositoryImpl(ResultReportImprovementRepository):
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

    def createResultReportImprovement(self, report):
        ResultReportImprovement.objects.create(report=report)

    def getResultReportImprovement(self, report):
        return ResultReportImprovement.objects.get(report=report)
