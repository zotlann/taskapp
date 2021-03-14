from django.urls import path
from . import views

urlpatterns = [
        path('create-task/',views.CreateTask, name='create-task'),
        path('view-tasks/' ,views.ViewTasks,  name='view-tasks'),
        path('edit-task/', views.EditTask, name='edit-task'),
]
