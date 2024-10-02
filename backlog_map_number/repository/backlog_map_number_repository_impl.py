from django.db import IntegrityError

from backlog_map_number.entity.backlog_map_number import BacklogMapNumber
from backlog_map_number.repository.backlog_map_number_repository import BacklogMapNumberRepository


class BacklogMapNumberRepositoryImpl(BacklogMapNumberRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance =  cls()
        return cls.__instance

    def create(self, backlog, backlogMapNumber):
        try:
            backlogMapNumber = BacklogMapNumber(backlog=backlog, map_number=backlogMapNumber)
            backlogMapNumber.save()

            return backlogMapNumber

        except IntegrityError:
            return None
