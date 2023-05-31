from django.shortcuts import render,get_object_or_404,redirect
from todos.models import TodoList
from todos.forms import TodoListForm


def todo_list_list(request):
    todos = TodoList.objects.all()
    context = {
       "todo_list_list": todos
    }
    return render(request, "todos/list.html", context)


def show_list(request, id):
    list = get_object_or_404(TodoList, id=id)
    context = {
        "list": list,
    }
    return render(request, "todos/detail.html", context)


def create_list(request):
#    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todolist = form.save()
            return redirect("todo_list_detail", id=todolist.id)

        context = {
            "form": form
        }

        return render(request, "todos/create.html", context)


def update_list(request, id):
    todolist = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todolist)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=todolist.id)
    else:
        form = TodoListForm(instance=todolist)

    context = {
        "form": form
    }
    return render(request, "todos/edit.html", context)
