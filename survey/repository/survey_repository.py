from abc import ABC, abstractmethod


class SurveyRepository(ABC):
    @abstractmethod
    def save(self, surveyNumber, surveyQuestionNumber, surveySelectionNumber):
        pass

    @abstractmethod
    def register(self, surveyID, surveyQuestionSentence, surveySelectionList):
        pass

    @abstractmethod
    def returnComponents(self, surveyNumber):
        pass
