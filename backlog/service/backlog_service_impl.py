from typing import List

from backlog.repository.backlog_repository_impl import BacklogRepositoryImpl
from backlog.service.backlog_service import BacklogService
from backlog_domain.repository.backlog_domain_repository_impl import BacklogDomainRepositoryImpl
from backlog_success_criteria.repository.backlog_success_criteria_repository_impl import \
    BacklogSuccessCriteriaRepositoryImpl
from backlog_success_criteria.service.backlog_success_criteria_service_impl import BacklogSuccessCriteriaServiceImpl
from backlog_todo.repository.backlog_todo_repository_impl import BacklogTodoRepositoryImpl


class BacklogServiceImpl(BacklogService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__backlogRepository = BacklogRepositoryImpl.getInstance()
            cls.__instance.__backlogDomainRepository = BacklogDomainRepositoryImpl.getInstance()
            cls.__instance.__backlogSuccessCriteriaRepository = BacklogSuccessCriteriaRepositoryImpl.getInstance()
            cls.__instance.__backlogTodoRepository = BacklogTodoRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createBacklog(self, backlogList):
        titleList = []
        domainList = []
        successCriteriaList = []
        todoList = []

        for backlog in backlogList:
            title, domain, successCriteria, taskList = (
                backlog['title'], backlog['domain'], backlog['success_criteria'], backlog['task_list'])
            titleList.append(title)
            domainList.append(domain)
            successCriteriaList.append(successCriteria)
            todoList.append(taskList)

        try:
            backlog = self.__backlogRepository.create(titleList)
            backlogDomain = self.__backlogDomainRepository.create(backlog, domainList)
            backlogSuccessCriteria = self.__backlogSuccessCriteriaRepository.create(backlog, successCriteriaList)
            backlogTodo = self.__backlogTodoRepository.create(backlog, todoList)
            return backlog
        except Exception as e:
            print('Error creating backlog:', e)
            raise e

