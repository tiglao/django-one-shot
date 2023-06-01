from django.forms import ModelForm
from todos.models import TodoList, TodoItem

class TodoListForm(ModelForm):
#	email_address = forms.EmailField(max_length=300)

	class Meta:
		model = TodoList
		fields = (
			"name",
		)


class TodoItemForm(ModelForm):
#	email_address = forms.EmailField(max_length=300)

	class Meta:
		model = TodoItem
		fields = (
			"task",
			"due_date",
			"is_completed",
			"list"
		)
