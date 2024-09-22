from survey.repository.survey_repository_impl import SurveyRepositoryImpl
from survey.service.survey_service import SurveyService


class SurveyServiceImpl(SurveyService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
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

    def registerNewSurvey(self, surveyID, surveyQuestionSentence, surveySelectionList):
        print(f"SurveyServiceImpl() -> registerNewSurvey()")
        return self.__surveyRepository.register(surveyID, surveyQuestionSentence, surveySelectionList)

    def readSurvey(self, Id):
        document = self.__surveyRepository.findDocumentById(Id)  # document class자체가 들어옴
        survey = self.__surveyRepository.findSurveyByDocument(document)
        questions = self.__surveyRepository.findQuestionBySurvey(survey)
        selections = self.__surveyRepository.findSelectionByQuestion(questions)

        questionList = []
        for question in questions:
            questionList.append(question.SurveyQuestionSentence)

        selectionList = []
        for selection in selections:
            selectList = []
            for select in selection:
                selectList.append(select.SurveySelectionSentence)
            selectionList.append(selectList)

        return questionList, selectionList

    def returnSurveyComponents(self, surveyNumber):
        print(f"SurveyServiceImpl() -> returnSurveyComponents")
        return self.__surveyRepository.returnComponents(surveyNumber)
