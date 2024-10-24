from report_skill.entity.report_skill import ResultReportSkill
from report_skill.repository.report_skill_repository import ResultReportSkillRepository


class ResultReportSkillRepositoryImpl(ResultReportSkillRepository):
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

    def create(self, skillList, skillset):
        resultReportSkillList = [ResultReportSkill(skill=skill, skillset=skillset) for skill in skillList]
        ResultReportSkill.objects.bulk_create(resultReportSkillList)

        return resultReportSkillList
