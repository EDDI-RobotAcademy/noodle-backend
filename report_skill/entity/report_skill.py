from django.db import models

from report_skill_set.entity.report_skill_set import ResultReportSkillSet


class ResultReportSkill(models.Model):
    id = models.AutoField(primary_key=True)
    skill = models.CharField(max_length=64)
    skillset = models.ForeignKey(ResultReportSkillSet, on_delete=models.CASCADE, related_name="skill")

    def __str__(self):
        return f"ResultReportSkillId: {self.id} -> ResultReportSkill: {self.skill} on ResultReportSkillsetId: {self.skill.id}"

    class Meta:
        db_table = "report_skill"
