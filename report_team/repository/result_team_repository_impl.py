from report_team.entity.report_team import ResultReportTeam
from report_team.repository.result_team_repository import ResultReportTeamRepository


class ResultReportTeamRepositoryImpl(ResultReportTeamRepository):
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

    def create(self):
        ResultReportTeam.objects.create()
