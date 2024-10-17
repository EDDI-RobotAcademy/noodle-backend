from report_usage.entity.report_usage import ResultReportUsage
from report_usage.repository.report_usage_repository import ResultReportUsageRepository


class ResultReportUsageRepositoryImpl(ResultReportUsageRepository):
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

    def createResultReportUsage(self, report, content):
        ResultReportUsage.objects.create(report=report, content=content)
