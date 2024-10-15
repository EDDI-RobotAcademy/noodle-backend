from django.db import IntegrityError

from backlog_status.entity.backlog_status import BacklogStatus
from backlog_status.repository.backlog_status_repository import BacklogStatusRepository


class BacklogStatusRepositoryImpl(BacklogStatusRepository):
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

    def create(self, backlog, backlogStatus):
        try:
            backlogStatus = BacklogStatus(backlog=backlog, status=backlogStatus)
            backlogStatus.save()

            return backlogStatus

        except IntegrityError:
            return None
