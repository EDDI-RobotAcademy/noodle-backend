from survey.entity.survey_answer import SurveyAnswer
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

    def saveSurveyAnswer(self, surveyNumber, surveySelectionNumber):
        print(f"SurveyServiceImpl() -> saveSurveyAnswer()")
        documentNumber = self.__surveyRepository.findDocumentById(surveyNumber)
        surveyID = self.__surveyRepository.findSurveyByDocument(documentNumber.id)

        surveyQuestions = self.__surveyRepository.findQuestionBySurvey(surveyID.id)
        surveyQuestionList = [component for component in surveyQuestions]

        if len(surveyQuestionList) != len(surveySelectionNumber):
            print('error occurred while saving answers! invalid matching components!')

        for i in range(len(surveyQuestionList)):
            surveyQuestion = surveyQuestionList[i]
            surveySelection = self.__surveyRepository.findSelectionBySurveyQuestionIDAndSelectionNumber(
                surveyQuestion, surveySelectionNumber[i])
            print(surveyQuestion, "<-->", surveySelection.id)
            SurveyAnswer.objects.create(
                SurveyQuestionID=surveyQuestion,
                SurveySelectionID=surveySelection
            )

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
        return self.__surveyRepository.returnComponents(surveyNumber, 0)

    def readSurveyResult(self, surveyNumber):
        print(f"SurveyServiceImpl()-> readSurveyResult")
        return self.__surveyRepository.returnComponents(surveyNumber, 1)

    def makeBulkInjection(self, questionList, answerList):
        print(f"SurveyServiceImpl() -> makeBulkInjection")
        queryInfo = []

        try:
            for i in range(len(questionList)):
                for answer in answerList:
                    print(questionList[i])
                    print(answer[i])
                    questionObject = self.__surveyRepository.findQuestionByQuestionSentence(questionList[i])
                    selectionObject = self.__surveyRepository.findSelectionBySelectionSentence(questionObject,
                                                                                               answer[i])
                    queryInfo.append(
                        SurveyAnswer(SurveyQuestionID=questionObject, SurveySelectionID=selectionObject))

            return queryInfo
        except Exception as e:
            print("error occured while creating queryInfo: ", e)

    def operateBulkInjection(self, bulkInjectionQueryList):
        print(f"SurveyServiceImpl() -> operateBulkInjection")
        self.__surveyRepository.operateBulkInjection(bulkInjectionQueryList)
