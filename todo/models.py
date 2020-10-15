from django.db import models

# Create your models here.
class ToDoTasks(models.Model):
    task_date =  models.DateTimeField()
    task = models.CharField(max_length=200)
    
