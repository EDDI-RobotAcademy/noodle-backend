from report_modify.entity.report_modify import ResultReportModify
from report_modify.repository.report_modify_repository import ResultReportModifyRepository


class ResultReportModifyRepositoryImpl(ResultReportModifyRepository):
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

    def modify(self, resultReportId, modifier):
        try:
            resultReportModify = ResultReportModify.objects.get(report_id=resultReportId)
            resultReportModify.modifier = modifier
            resultReportModify.save()

        except ResultReportModify.DoesNotExist:
            ResultReportModify.objects.create(modifier=modifier, report_id=resultReportId)
