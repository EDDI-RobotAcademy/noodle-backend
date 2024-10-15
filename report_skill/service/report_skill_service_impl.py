from report_skill.repository.report_skill_repository_impl import ResultReportSkillRepositoryImpl
from report_skill.service.report_skill_service import ResultReportSkillService


class ResultReportSkillServiceImpl(ResultReportSkillService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportSkillRepository = ResultReportSkillRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createResultReportSkill(self, skill, skillSetId):
        self.__resultReportSkillRepository.create(skill, skillSetId)
