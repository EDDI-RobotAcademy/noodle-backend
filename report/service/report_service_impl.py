from report.repository.report_repository_impl import ResultReportRepositoryImpl
from report.service.report_service import ResultReportService
from report_completion.repository.report_completion_repository_impl import ResultReportCompletionRepositoryImpl
from report_completion_maintain.repository.report_completion_maintain_repository_impl import \
    ResultReportCompletionMaintainRepositoryImpl
from report_completion_secure.repository.report_completion_secure_repository_impl import \
    ResultReportCompletionSecureRepositoryImpl
from report_completion_total.repository.report_completion_total_repository_impl import \
    ResultReportCompletionTotalRepositoryImpl
from report_feature.repository.report_feature_repository_impl import ResultReportFeatureRepositoryImpl
from report_feature_content.repository.report_feature_content_repository_impl import \
    ResultReportFeatureContentRepositoryImpl
from report_improvement.repository.report_improvement_repository_impl import ResultReportImprovementRepositoryImpl
from report_improvement_content.repository.report_improvement_content_repository_impl import \
    ResultReportImprovementContentRepositoryImpl
from report_modify.repository.report_modify_repository_impl import ResultReportModifyRepositoryImpl
from report_overview.repository.report_overview_repository_impl import ResultReportOverviewRepositoryImpl
from report_skill.repository.report_skill_repository_impl import ResultReportSkillRepositoryImpl
from report_skill_set.repository.result_skill_set_repository_impl import ResultReportSkillSetRepositoryImpl
from report_team.repository.result_team_repository_impl import ResultReportTeamRepositoryImpl
from report_team_member.repository.report_team_member_repository_impl import ResultReportTeamMemberRepositoryImpl
from report_title.repository.report_title_repository_impl import ResultReportTitleRepositoryImpl
from report_usage.repository.report_usage_repository_impl import ResultReportUsageRepositoryImpl


class ResultReportServiceImpl(ResultReportService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__resultReportRepository = ResultReportRepositoryImpl.getInstance()
            cls.__instance.__resultReportModifyRepository = ResultReportModifyRepositoryImpl.getInstance()
            cls.__instance.__resultReportOverviewRepository = ResultReportOverviewRepositoryImpl.getInstance()
            cls.__instance.__resultReportTitleRepository = ResultReportTitleRepositoryImpl.getInstance()
            cls.__instance.__resultReportSkillRepository = ResultReportSkillRepositoryImpl.getInstance()
            cls.__instance.__resultReportSkillSetRepository = ResultReportSkillSetRepositoryImpl.getInstance()
            cls.__instance.__resultReportTeamRepository = ResultReportTeamRepositoryImpl.getInstance()
            cls.__instance.__resultReportTeamMemberRepository = ResultReportTeamMemberRepositoryImpl.getInstance()
            cls.__instance.__resultReportFeatureRepository = ResultReportFeatureRepositoryImpl.getInstance()
            cls.__instance.__resultReportFeatureContentRepository = ResultReportFeatureContentRepositoryImpl.getInstance()
            cls.__instance.__resultReportUsageRepository = ResultReportUsageRepositoryImpl.getInstance()
            cls.__instance.__resultReportImprovementRepository = ResultReportImprovementRepositoryImpl.getInstance()
            cls.__instance.__resultReportImprovementContentRepository = ResultReportImprovementContentRepositoryImpl.getInstance()
            cls.__instance.__resultReportCompletionRepository = ResultReportCompletionRepositoryImpl.getInstance()
            cls.__instance.__resultReportCompletionSecureRepository = ResultReportCompletionSecureRepositoryImpl.getInstance()
            cls.__instance.__resultReportCompletionMaintainRepository = ResultReportCompletionMaintainRepositoryImpl.getInstance()
            cls.__instance.__resultReportCompletionTotalRepository = ResultReportCompletionTotalRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createResultReport(self, username, title, overview, teamMemberList,
                           skillList, featureList, usage, improvementList, completionList):
        report = self.__resultReportRepository.create(username)
        modifier = self.__resultReportModifyRepository.create(report, username)
        reportTitle = self.__resultReportTitleRepository.create(report, title)
        reportOverview = self.__resultReportOverviewRepository.createResultReportOverview(overview, report)
        # TODO: Frontend에서 Team 관련 내용 어떻게 넘길지 결정해야 함(AI Client에서는 Team 관련 내용을 생성하지 않기 때문)
        reportTeam = self.__resultReportTeamRepository.create(report)
        reportTeamMember = self.__resultReportTeamMemberRepository.createResultReportTeamMember(teamMemberList,
                                                                                                reportTeam)
        reportSkillSet = self.__resultReportSkillSetRepository.create(report)
        reportSkill = self.__resultReportSkillRepository.create(skillList, reportSkillSet)
        reportFeature = self.__resultReportFeatureRepository.createResultReportFeature(report)
        reportFeatureContent = self.__resultReportFeatureContentRepository.createResultReportFeatureContent(featureList,
                                                                                                            reportFeature)
        reportUsage = self.__resultReportUsageRepository.createResultReportUsage(report, usage)
        reportImprovement = self.__resultReportImprovementRepository.createResultReportImprovement(report)
        reportImprovementContent = self.__resultReportImprovementContentRepository.createResultReportImprovementContent(
            reportImprovement, improvementList)
        reportCompletion = self.__resultReportCompletionRepository.createResultReportCompletion(report)
        reportCompletionSecure = self.__resultReportCompletionSecureRepository.createResultReportCompletionSecure(
            reportCompletion, completionList[0][0], completionList[0][1])
        reportCompletionMaintain = self.__resultReportCompletionMaintainRepository.createResultReportCompletionMaintain(
            reportCompletion, completionList[1][0], completionList[1][1])
        reportCompletionTotal = self.__resultReportCompletionTotalRepository.createResultReportCompletionTotal(
            reportCompletion, completionList[2][0], completionList[2][1])

        return report

    def list(self, query):
        if not query:
            resultReportList = self.__resultReportRepository.getAllResultReportList()
            resultReportTitleList = self.__resultReportTitleRepository.getAllResultReportTitleList()
        else:
            resultReportTitleList = self.__resultReportTitleRepository.getSearchResultReportTitle(query)
            resultReportList = []
            for resultReportTitle in resultReportTitleList:
                resultReport = self.__resultReportRepository.getReportById(resultReportTitle.id)
                resultReportList.append(resultReport)

        resultReportIdList = [resultReport.id for resultReport in resultReportList]
        resultReportCreatorList = [resultReport.creator for resultReport in resultReportList]

        resultReportTeamMemberDepartmentList = []
        resultReportFeatureContentList = []

        for i in range(len(resultReportList)):
            resultReportTeam = (
                self.__resultReportTeamRepository.getResultReportTeamByResultReport(resultReportList[i]))
            resultReportTeamMember = (
                self.__resultReportTeamMemberRepository.getResultReportTeamMemberByResultReportTeamAndName(
                    resultReportTeam, resultReportCreatorList[i]))
            if resultReportTeamMember:
                resultReportTeamMemberDepartmentList.append(resultReportTeamMember.department)
            else:
                resultReportTeamMemberDepartmentList.append(None)

            resultReportFeature = (
                self.__resultReportFeatureRepository.getResultReportFeatureByResultReport(resultReportList[i]))
            resultReportFeatureContent = (
                self.__resultReportFeatureContentRepository.getResultReportFeatureListByResultReportFeature(
                    resultReportFeature))
            resultReportFeatureContentList.append(resultReportFeatureContent[0])

        result = []
        for i in range(len(resultReportIdList)):
            data = {
                'resultReportId': resultReportIdList[i],
                'resultReportTitle': resultReportTitleList[i].title,
                'creator': resultReportCreatorList[i],
                'resultReportFeature': resultReportFeatureContentList[i],
                'creatorDepartment': resultReportTeamMemberDepartmentList[i]
            }
            result.append(data)

        return result

    def read(self, resultReportId):
        report = self.__resultReportRepository.getReportById(resultReportId)
        title = self.__resultReportTitleRepository.getResultReportTitleByResultReport(report).title
        overview = self.__resultReportOverviewRepository.getResultReportOverviewByResultReport(report).overview
        team = self.__resultReportTeamRepository.getResultReportTeamByResultReport(report)
        teamMemberList = self.__resultReportTeamMemberRepository.getResultReportTeamMemberListByResultReportTeam(team)
        skillSet = self.__resultReportSkillSetRepository.getResultReportSkillSetByResultReport(report)
        skillList = self.__resultReportSkillRepository.getResultReportSkillListByResultReportSkillSet(skillSet)
        feature = self.__resultReportFeatureRepository.getResultReportFeatureByResultReport(report)
        featureList = self.__resultReportFeatureContentRepository.getResultReportFeatureListByResultReportFeature(
            feature)
        usage = self.__resultReportUsageRepository.getResultReportUsageByResultReport(report).content
        improvement = self.__resultReportImprovementRepository.getResultReportImprovement(report)
        improvementList = self.__resultReportImprovementContentRepository.getResultReportImprovementListByResultReportImprovement(
            improvement)
        completion = self.__resultReportCompletionRepository.getResultRepositoryCompletionByResultReport(report)
        secure = self.__resultReportCompletionSecureRepository.getResultReportCompletionSecureByResultReportCompletion(
            completion)
        maintain = self.__resultReportCompletionMaintainRepository.getResultReportCompletionMaintainByResultReportCompletion(
            completion)
        total = self.__resultReportCompletionTotalRepository.getResultReportCompletionTotalByResultReportCompletion(
            completion)
        completionList = [["보안", secure.score, secure.detail],
                          ["유지 보수", maintain.score, maintain.detail],
                          ["종합", total.score, total.detail]]

        return {
            "data": {
                "title": title,
                "overview": overview,
                "teamMemberList": teamMemberList,
                "skillList": skillList,
                "featureList": featureList,
                "usage": usage,
                "improvementList": improvementList,
                "completionList": completionList
            }
        }

    def modify(self, id, user, modifiedReport):
        report = self.__resultReportRepository.getReportById(id)
        realname = self.__resultReportModifyRepository.getModifierByResultReport(report).modifier
        if realname == user:
            titleObj = self.__resultReportTitleRepository.getResultReportTitleByResultReport(report)
            self.__resultReportTitleRepository.modify(titleObj, modifiedReport['title'])

            overviewObj = self.__resultReportOverviewRepository.getResultReportOverviewByResultReport(report)
            self.__resultReportOverviewRepository.modify(overviewObj, modifiedReport['overview'])

            teamObj = self.__resultReportTeamRepository.getResultReportTeamByResultReport(report)
            self.__resultReportTeamMemberRepository.modify(teamObj, modifiedReport['teamMemberList'])

            skillObj = self.__resultReportSkillSetRepository.getResultReportSkillSetByResultReport(report)
            self.__resultReportSkillRepository.modify(skillObj, modifiedReport['skillList'])

            featureObj = self.__resultReportFeatureRepository.getResultReportFeatureByResultReport(report)
            self.__resultReportFeatureContentRepository.modify(featureObj, modifiedReport['featureList'])

            usageObj = self.__resultReportUsageRepository.getResultReportUsageByResultReport(report)
            self.__resultReportUsageRepository.modify(usageObj, modifiedReport['usage'])

            improvementObj = self.__resultReportImprovementRepository.getResultReportImprovement(report)
            self.__resultReportImprovementContentRepository.modify(improvementObj, modifiedReport['improvements'])

            return True

        else:
            return False

    def delete(self, id, user):
        report = self.__resultReportRepository.getReportById(id)
        realname = self.__resultReportModifyRepository.getModifierByResultReport(report).modifier
        if realname == user:
            self.__resultReportTitleRepository.delete(report)

            self.__resultReportOverviewRepository.delete(report)

            teamObj = self.__resultReportTeamRepository.getResultReportTeamByResultReport(report)
            self.__resultReportTeamMemberRepository.delete(teamObj)
            self.__resultReportTeamRepository.delete(report)

            skillObj = self.__resultReportSkillSetRepository.getResultReportSkillSetByResultReport(report)
            self.__resultReportSkillRepository.delete(skillObj)
            self.__resultReportSkillSetRepository.delete(report)

            featureObj = self.__resultReportFeatureRepository.getResultReportFeatureByResultReport(report)
            self.__resultReportFeatureContentRepository.delete(featureObj)
            self.__resultReportFeatureRepository.delete(report)

            self.__resultReportUsageRepository.delete(report)

            improvementObj = self.__resultReportImprovementRepository.getResultReportImprovement(report)
            self.__resultReportImprovementContentRepository.delete(improvementObj)
            self.__resultReportImprovementRepository.delete(report)

            completionObj = self.__resultReportCompletionRepository.getResultRepositoryCompletionByResultReport(report)
            self.__resultReportCompletionSecureRepository.delete(completionObj)
            self.__resultReportCompletionMaintainRepository.delete(completionObj)
            self.__resultReportCompletionTotalRepository.delete(completionObj)
            self.__resultReportCompletionRepository.delete(report)

            self.__resultReportModifyRepository.delete(report)
            self.__resultReportRepository.delete(id)
            return True

        else:
            return False

    def validateUser(self, id, user):
        report = self.__resultReportRepository.getReportById(id)
        realname = self.__resultReportModifyRepository.getModifierByResultReport(report).modifier
        if user == realname:
            return True
        else:
            return False
