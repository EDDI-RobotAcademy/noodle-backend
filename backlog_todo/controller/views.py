from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from backlog_todo.service.backlog_todo_service_impl import BacklogTodoServiceImpl


class BacklogTodoView(viewsets.ViewSet):
    backlogTodoService = BacklogTodoServiceImpl.getInstance()

    def createBacklogTodo(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        todo = data.get('todo')

        createdBacklogTodo = self.backlogTodoService.createBacklogTodo(backlogId, todo)

        return Response(createdBacklogTodo, status=status.HTTP_200_OK)