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
        return redirect('/')
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
        return redirect(ViewTasks)
    #if we haven't recieved the task data, display the form
    else:
        form = TaskForm()
        return render(request,'create_task.html',{'form': form})

#view for the view-tasks url
def ViewTasks(request):
    #if the user isn't logged in, redirect to the homepage
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        #if there is an id property in the query string, mark that task as completed
        task_id = request.GET.get('id')
        if task_id is not None:
            task_id = int(task_id)
            task = TaskModel.objects.get(id=task_id)
            task.is_completed = True
            task.save()
        #if the user is logged in, query the db for their tasks
        #and dispaly them
        username = request.user.username
        tasks = TaskModel.objects.all().filter(username=username,is_completed=False).order_by('due_date')
        return render(request,'view_tasks.html',{'obj':tasks})

#view for the view-complete url
def ViewCompletedTasks(request):
    #if the user isn't logged in, redirect to the homepage
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        #if there is an id property in the query string, mark that task as incomplete
        task_id = request.GET.get('id')
        if task_id is not None:
            task_id = int(task_id)
            task = TaskModel.objects.get(id=task_id)
            task.is_completed = False
            task.save()
        #display the completed tasks
        username = request.user.username
        tasks = TaskModel.objects.all().filter(username=username,is_completed=True).order_by('-due_date')
        return render(request,'view_completed.html',{'obj':tasks})

#view for the edit-task url
def EditTask(request):
    #if the user isn't logged in, redirect to the homepage
    if not request.user.is_authenticated:
        return redirect('/')
    #get the id of the task to edit
    task_id = int(request.GET.get('id'))
    task = TaskModel.objects.get(id=task_id)
    #if the method is POST, update the task object
    if request.method == 'POST':
        task.title = request.POST['title']
        task.details = request.POST['details']
        task.due_date = request.POST['due_date']
        task.save()
        return redirect(ViewTasks)
    #if the task doesn't belong to the current user, redirect to the homepage
    if task.username != request.user.username:
        return redirect('/')
    #else display the task
    else:
        date = task.due_date
        form = TaskForm(initial={'title':task.title,'due_date':datetime.strftime(task.due_date,'%Y-%m-%dT%H:%M'),'details':task.details})
        return render(request,'edit_task.html',{'form':form})

