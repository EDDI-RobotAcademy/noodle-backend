from abc import abstractmethod, ABC


class ResultReportService(ABC):
    @abstractmethod
    def createResultReport(self, username, title, overview, teamMemberList,
                           skillList, featureList, usage, improvementList, completionList):
        pass

    @abstractmethod
    def list(self, query):
        pass

    @abstractmethod
    def read(self, resultReportId):
        pass

    @abstractmethod
    def modify(self, id, user, modifiedReport):
        pass

    @abstractmethod
    def delete(self, id, user):
        pass

    @abstractmethod
    def validateUser(self, id, user):
        pass
