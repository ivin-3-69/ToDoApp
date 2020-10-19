from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from . import models

def base(request):
    task_objects = models.ToDoTasks.objects.all()
    context = {
        "tasks" : task_objects
    }
    print(task_objects)
    #models.ToDoTasks.objects.all().delete()
    return render(request, "todo/index.html" ,context)

def add(request):
    new_event = request.POST.get("new-task")
    present = timezone.now()
    models.ToDoTasks.objects.create(task_date = present ,task = new_event)
    return HttpResponseRedirect("/todo/")
    
    