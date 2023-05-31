from django.db import models

# Create your models here.
class TodoList(models.Model):
        name = models.CharField(max_length=200)
        created_on = models.DateTimeField(auto_now_add=True)
