from django.db import models

from report_team.entity.report_team import ResultReportTeam


class ResultReportTeamMember(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    role = models.CharField(max_length=64)
    team = models.ForeignKey(ResultReportTeam, on_delete=models.CASCADE, related_name="team_member")

    def __str__(self):
        return f"ResultReportTeamMemberId: {self.id} -> Name: {self.name}, Role: {self.role} works in {self.team.id}"

    class Meta:
        db_table = "report_team_member"
