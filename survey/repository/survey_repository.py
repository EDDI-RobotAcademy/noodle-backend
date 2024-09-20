from abc import ABC, abstractmethod


class SurveyRepository(ABC):
    @abstractmethod
    def save(self, surveyNumber, surveyQuestionNumber, surveySelectionNumber):
        pass

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
    def returnComponents(self, surveyNumber):
        pass
