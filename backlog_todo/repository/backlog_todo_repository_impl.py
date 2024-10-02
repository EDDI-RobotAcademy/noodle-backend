from django.db import IntegrityError

from backlog_todo.entity.backlog_tod import BacklogTodo
from backlog_todo.repository.backlog_todo_repository import BacklogTodoRepository


class BacklogTodoRepositoryImpl(BacklogTodoRepository):
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

    def create(self, backlog, todo):
        try:
            todo = BacklogTodo(backlog=backlog, todo=todo)
            todo.save()

            return todo
        except IntegrityError:
            return None

