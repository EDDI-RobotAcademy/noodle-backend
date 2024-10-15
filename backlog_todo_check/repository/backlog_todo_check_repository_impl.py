from django.db import IntegrityError

from backlog_todo_check.entity.backlog_todo_check import BacklogTodoCheck
from backlog_todo_check.repository.backlog_todo_check_repository import BacklogTodoCheckRepository


class BacklogTodoCheckRepositoryImpl(BacklogTodoCheckRepository):
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

    def create(self, todo, isChecked):
        try:
            backlogTodoCheck = BacklogTodoCheck(backlogTodo=todo, isChecked=isChecked)
            backlogTodoCheck.save()

            return backlogTodoCheck

        except IntegrityError:
            return None



