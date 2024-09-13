from survey.repository.survey_repository_impl import SurveyRepositoryImpl
from survey.service.survey_service import SurveyService


class SurveyServiceImpl(SurveyService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance.__surveyRepository = SurveyRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def saveSurveyAnswer(self, surveyNumber, surveyQuestionNumber, surveySelectionNumber):
        print(f"SurveyServiceImpl() -> saveSurveyAnswer()")
        self.__surveyRepository.save(surveyNumber, surveyQuestionNumber, surveySelectionNumber)

    def registerNewSurvey(self, surveyID, surveyQuestionNumber, surveyQuestionSentence, surveySelectionList):
        print(f"SurveyServiceImpl() -> registerNewSurvey()")
        self.__surveyRepository.register(surveyID, surveyQuestionNumber, surveyQuestionSentence, surveySelectionList)
