from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from backlog.entity.backlog import Backlog
from backlog.repository.backlog_repository import BacklogRepository


class BacklogRepositoryImpl(BacklogRepository):
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

    def create(self, titleList):
        backlogs = [Backlog(title=title) for title in titleList]

        try:
            backlogList = Backlog.objects.bulk_create(backlogs)
            return backlogList

        except IntegrityError:
            return None

    def findById(self, backlogId):
        try:
            backlog = Backlog.objects.get(id=backlogId)
            return backlog
        except ObjectDoesNotExist:
            raise ValueError(f"Backlog with id {backlogId} does not exist")
        except Exception as e:
            error = f'{e}:error while loading backlog'
            raise error

    def getTotalNumberOfBacklog(self):
        return Backlog.objects.count()
