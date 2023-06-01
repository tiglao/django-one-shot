from django.urls import path
from todos.views import todo_list_list, show_list, create_list, update_list, delete_list, create_item


urlpatterns = [
    path("todos/", todo_list_list, name="todo_list_list"),
    path("todos/<int:id>/", show_list, name="todo_list_detail"),
    path("todos/create/", create_list, name="todo_list_create"),
    path("todos/<int:id>/edit/", update_list, name="todo_list_edit"),
    path("todos/<int:id>/delete/", delete_list, name="todo_list_delete"),
    path("todos/items/create/", create_item, name="todo_item_create"),
]
