from abc import ABC, abstractmethod


class SurveyRepository(ABC):
    @abstractmethod
    def save(self, surveyNumber, surveyQuestionNumber, surveySelectionNumber):
        pass
