from django.urls import path
from todos.views import todo_list_list, show_list, create_list, update_list


urlpatterns = [
    path("", todo_list_list, name="todo_list_list"),
    path("<int:id>/", show_list, name="todo_list_detail"),
    path("create/", create_list , name="todo_list_create"),
    path("<int:id>/edit/", update_list, name="todo_list_edit"),
]
