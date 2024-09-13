from abc import ABC, abstractmethod


class SurveyService(ABC):
    @abstractmethod
    def saveSurveyAnswer(self, surveyNumber, surveyQuestionNumber, surveySelectionNumber):
        pass
