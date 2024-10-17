from report_skill.repository.report_skill_repository_impl import ResultReportSkillRepositoryImpl
from report_skill.service.report_skill_service import ResultReportSkillService
from report_skill_set.repository.result_skill_set_repository_impl import ResultReportSkillSetRepositoryImpl


class ResultReportSkillServiceImpl(ResultReportSkillService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportSkillRepository = ResultReportSkillRepositoryImpl.getInstance()
            cls.__instance.__resultReportSkillSetRepository = ResultReportSkillSetRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createResultReportSkill(self, skill, skillSetId):
        skillset = self.__resultReportSkillSetRepository.getResultReportSkillSetById(skillSetId)
        self.__resultReportSkillRepository.create(skill, skillset)
