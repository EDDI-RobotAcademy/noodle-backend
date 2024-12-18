from report_improvement_content.entity.report_improvement_content import ResultReportImprovementContent
from report_improvement_content.repository.report_improvement_content_repository import \
    ResultReportImprovementContentRepository


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
        resultReportImprovementContentList = [ResultReportImprovementContent(content=content, improvement=report)
                                              for content in reportImprovementContentList]
        ResultReportImprovementContent.objects.bulk_create(resultReportImprovementContentList)

        return resultReportImprovementContentList

    def getResultReportImprovementListByResultReportImprovement(self, improvement):
        resultReportImprovements = ResultReportImprovementContent.objects.filter(improvement=improvement)
        resultReportImprovementList = [improvement.content for improvement in resultReportImprovements]

        return resultReportImprovementList

    def modify(self, improvementObj, improvements):
        ResultReportImprovementContent.objects.filter(improvement=improvementObj).delete()

        resultReportImprovementContentList = [
            ResultReportImprovementContent(content=content, improvement=improvementObj)
            for content in improvements]
        ResultReportImprovementContent.objects.bulk_create(resultReportImprovementContentList)

    def delete(self, improvementObj):
        ResultReportImprovementContent.objects.filter(improvement=improvementObj).delete()
