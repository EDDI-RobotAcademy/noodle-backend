from abc import ABC, abstractmethod


class SurveyRepository(ABC):

    @abstractmethod
    def register(self, surveyID, surveyQuestionSentence, surveySelectionList):
        pass

    @abstractmethod
    def findDocumentById(self, Id):
        pass

    @abstractmethod
    def findSurveyByDocument(self, document):
        pass

    @abstractmethod
    def findQuestionBySurvey(self, survey):
        pass

    @abstractmethod
    def findSelectionByQuestion(self, question):
        pass

    @abstractmethod
    def findSelectionBySurveyQuestionIDAndSelectionNumber(self, questionID, selectionNumber):
        pass

    @abstractmethod
    def returnComponents(self, surveyNumber, flag):
        pass

    @abstractmethod
    def findQuestionByQuestionSentence(self, questionSentence):
        pass

    @abstractmethod
    def findSelectionBySelectionSentence(self, questionID, answer):
        pass

    @abstractmethod
    def operateBulkInjection(self, bulkInjectionQueryList):
        pass
