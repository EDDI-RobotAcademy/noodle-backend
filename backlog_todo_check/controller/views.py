from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response

from backlog_todo_check.service.backlog_todo_check_service_impl import BacklogTodoCheckServiceImpl


class BacklogTodoCheckView(views.View):
    backlogTodoCheckService = BacklogTodoCheckServiceImpl.getInstance()

    def createBacklogTodoCheck(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        isChecked = data.get('isChecked')

        createdBacklogTodoCheck = self.backlogTodoCheckService.createBacklogTodoCheck(backlogId, isChecked)

        return Response(createdBacklogTodoCheck, status=status.HTTP_200_OK)