from django.db import IntegrityError

from backlog_domain.entity.backlog_domain import BacklogDomain
from backlog_domain.repository.backlog_domain_repository import BacklogDomainRepository


class BacklogDomainRepositoryImpl(BacklogDomainRepository):
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

    def create(self, backlog, domain):
        try:
            backlogDomain = BacklogDomain(backlog=backlog, domain=domain)
            backlogDomain.save()

            return backlogDomain

        except IntegrityError:
            return None