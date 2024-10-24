from report_overview.entity.report_overview import ResultReportOverview
from report_overview.repository.report_overview_repository import ResultReportOverviewRepository


class ResultReportOverviewRepositoryImpl(ResultReportOverviewRepository):
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

    def createResultReportOverview(self, overview, report):
        resultReportOverview = ResultReportOverview.objects.create(overview=overview, report=report)

        return resultReportOverview
