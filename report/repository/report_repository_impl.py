from report.entity.report import ResultReport
from report.repository.report_repository import ResultReportRepository


class ResultReportRepositoryImpl(ResultReportRepository):
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

    def create(self, creator):
        return ResultReport.objects.create(creator=creator)


