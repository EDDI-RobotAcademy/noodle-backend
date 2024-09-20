from abc import ABC, abstractmethod


class SurveyService(ABC):
    @abstractmethod
    def saveSurveyAnswer(self, surveyNumber, surveyQuestionNumber, surveySelectionNumber):
        pass

    @abstractmethod
    def registerNewSurvey(self, surveyID, surveyQuestionSentence, surveySelectionList):
        pass

    @abstractmethod
    def readSurvey(self, Id):
        pass

