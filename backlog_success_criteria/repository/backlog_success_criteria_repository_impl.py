from django.db import IntegrityError

from backlog_success_criteria.entity.backlog_success_criteria import BacklogSuccessCriteria
from backlog_success_criteria.repository.backlog_success_criteria_repository import BacklogSuccessCriteriaRepository


class BacklogSuccessCriteriaRepositoryImpl(BacklogSuccessCriteriaRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, backlog, successCriteria):
        try:
            successCriteria = BacklogSuccessCriteria(backlog=backlog, successCriteria=successCriteria)
            successCriteria.save()

            return successCriteria

        except IntegrityError:
            return None
