from django.db.models.expressions import result

from report.repository.report_repository_impl import ResultReportRepositoryImpl
from report_skill_set.repository.result_skill_set_repository_impl import ResultReportSkillSetRepositoryImpl
from report_skill_set.service.report_skill_set_service import ResultReportSkillSetService


class ResultReportSkillSetServiceImpl(ResultReportSkillSetService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportSkillSetRepository = ResultReportSkillSetRepositoryImpl.getInstance()
            cls.__instance.__resultReportRepository = ResultReportRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createResultReportSkillSet(self, resultReportId):
        report = self.__resultReportRepository.getReportById(resultReportId)
        self.__resultReportSkillSetRepository.create(report)
