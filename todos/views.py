from django.shortcuts import render
from todos.models import TodoList


def todo_list_list(request):
    todo_list_list = TodoList.objects.all()
    context = {
       "todo_list_list": todo_list_list
    }
    return render(request, "todos/list.html", context)
