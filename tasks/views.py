from django.shortcuts import render
from .forms import TaskForm
from django.http import HttpResponse
from datetime import datetime
from.models import TaskModel
from django.shortcuts import redirect

#view for the create-task url
def CreateTask(request):
    #if the user isn't logged in, redirect to the homepage
    if not request.user.is_authenticated:
        return redirect('')
    #if we recieved the task data in the form, create
    #an instace of our Task model and save it to the db
    #and show a screen indicating the task was saved
    if request.method == 'POST':
        due_date = request.POST['due_date']
        title    = request.POST['title']
        details  = request.POST['details']
        username = request.user.username
        task_instance = TaskModel.objects.create(username=username, title=title, due_date=due_date, details=details, is_completed=False)
        task_instance.save()
        return HttpResponse("Task has been saved.")
    #if we haven't recieved the task data, display the form
    else:
        form = TaskForm()
        return render(request,'create_task.html',{'form': form})

#view for the view-tasks url
def ViewTasks(request):
    #if the user isn't logged in, redirect to the homepage
    if not request.user.is_authenticated:
        return redirect('')
    #if the user is logged in, query the db for their tasks
    #and dispaly them
    else:
        username = request.user.username
        tasks = TaskModel.objects.all().filter(username=username)
        ret_str = ''
        for task in tasks:
            ret_str = ret_str + str(task)
        return HttpResponse(ret_str)
