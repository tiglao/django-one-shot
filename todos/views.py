from django.shortcuts import render,get_object_or_404
from todos.models import TodoList


def todo_list_list(request):
    todo_list_list = TodoList.objects.all()
    context = {
       "todo_list_list": todo_list_list
    }
    return render(request, "todos/list.html", context)


def show_list(request, id):
    list = get_object_or_404(TodoList, id=id)
    context = {
        "list": list,
    }
    return render(request, "todos/detail.html", context)
