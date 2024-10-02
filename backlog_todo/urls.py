from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backlog_todo.controller.views import BacklogTodoView

router = DefaultRouter()
router.register(r'backlog_todo', BacklogTodoView, basename='backlog-todo')

urlpatterns = [
    path('', include(router.urls)),
    path('create', BacklogTodoView.as_view({'post': 'createBacklogTodo'}), name='create-backlog-todo')
]