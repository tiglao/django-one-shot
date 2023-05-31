from django.forms import ModelForm
from todos.models import TodoList

class TodoListForm(ModelForm):
#	email_address = forms.EmailField(max_length=300)

	class Meta:
		model = TodoList
		fields = (
			"name",
		)
