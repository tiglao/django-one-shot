from django.urls import path
from todos.views import todo_list_list,show_list

urlpatterns = [
    path("todos/", todo_list_list, name="todo_list_list"),
    path('todos/<int:id>/', show_list, name="todo_list_detail"),
]
