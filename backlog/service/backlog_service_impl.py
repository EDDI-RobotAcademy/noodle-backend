import json
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

        print(f"titleList:", titleList)
        print(f"domainList:", domainList)
        print(f"successCriteriaList:", successCriteriaList)
        print(f"todoList:", todoList)

        try:
            totalLength = self.__backlogRepository.getTotalNumberOfBacklog()
            backlogs = self.__backlogRepository.create(titleList)
            print(f"backlogs: {backlogs}")
            for i in range(len(backlogs)):
                backlog = self.__backlogRepository.findById(totalLength + i + 1)
                backlogDomain = self.__backlogDomainRepository.create(backlog, domainList[i])
                backlogSuccessCriteria = self.__backlogSuccessCriteriaRepository.create(backlog, successCriteriaList[i])
                backlogTodo = self.__backlogTodoRepository.create(backlog, todoList[i])

            return backlogs, json.dumps({"startIdx": totalLength + 1, "endIdx": totalLength + len(backlogs)})
        except Exception as e:
            print('Error creating backlog:', e)
            raise e

    def getBacklogs(self, startIdx, endIdx):
        backlogList = []
        toDoList = []
        try:
            for i in range(startIdx, endIdx):
                backlog = self.__backlogRepository.findById(i)
                domain = self.__backlogDomainRepository.findById(backlog)
                successCriteria = self.__backlogSuccessCriteriaRepository.findById(backlog)
                toDo = self.__backlogTodoRepository.findByBacklog(backlog)
                for object in toDo:
                    toDoList.append(object.todo)

                backlogList.append({
                    "Title": backlog.title,
                    "Success Criteria": successCriteria.successCriteria,
                    "Domain Separation": domain.domain,
                    "Task List": toDoList
                })

            return backlogList

        except Exception as e:
            print(e)
            raise e
