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

    def create(self, resultReportId, modifier):
        ResultReportModify.objects.create(modifier=modifier, report_id=resultReportId)
