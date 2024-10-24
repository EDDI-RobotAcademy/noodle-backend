from report_improvement_content.entity.report_improvement_content import ResultReportImprovementContent
from report_improvement_content.repository.report_improvement_content_repository import ResultReportImprovementContentRepository


class ResultReportImprovementContentRepositoryImpl(ResultReportImprovementContentRepository):
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

    def createResultReportImprovementContent(self, report, reportImprovementContentList):
        resultReportImprovementContentList = [ResultReportImprovementContent(content=content, report=report)
                                              for content in reportImprovementContentList]
        ResultReportImprovementContent.objects.bulk_create(resultReportImprovementContentList)

        return resultReportImprovementContentList
