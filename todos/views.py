from django.shortcuts import render,get_object_or_404,redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm, TodoItemForm


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


def delete_list(request, id):
    todolist = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        todolist.delete()
        return redirect("todo_list_list")
    return render(request, "todos/delete.html")

def create_item(request):
#    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todolist = form.save()
            return redirect("todo_list_detail", id=todolist.list.id)

        context = {
            "form": form
        }

        return render(request, "todos/create_task.html", context)


def update_item(request, id):
    todolist = get_object_or_404(TodoList, id=id)
    todoitem = get_object_or_404(TodoItem, id=id)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=todoitem)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=todolist.id)
    else:
        form = TodoItemForm(instance=todoitem)

    context = {
        "form": form
    }

    return render(request, "todos/edit_task.html", context)
