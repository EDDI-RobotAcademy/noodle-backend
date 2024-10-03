from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backlog_todo_check.controller.views import BacklogTodoCheckView

router = DefaultRouter()
router.register(r'backlog_todo_check', BacklogTodoCheckView, basename='backlog-todo-check')

urlpatterns = [
    path('', include(router.urls)),
    path('create', BacklogTodoCheckView.as_view({'post': 'createBacklogTodoCheck'}), name='create-backlog-todo-check'),
]