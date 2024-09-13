from abc import ABC, abstractmethod


class SurveyService(ABC):
    @abstractmethod
    def saveSurveyAnswer(self, surveyNumber, surveyQuestionNumber, surveySelectionNumber):
        pass

    @abstractmethod
    def registerNewSurvey(self, surveyID, surveyQuestionNumber, surveyQuestionSentence, surveySelectionList):
        pass
