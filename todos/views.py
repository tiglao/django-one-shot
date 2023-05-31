from django.shortcuts import render,get_object_or_404,redirect
from todos.models import TodoList
from todos.forms import TodoListForm


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


def create_list(request):
#    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect("todo_list_detail", id=instance.id)

        context = {
            "form": form
        }

        return render(request, "todos/create.html", context)
