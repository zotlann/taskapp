from django.db import models
from datetime import datetime

class TaskModel(models.Model):
    #Each task has an associated user, a title, a due date, details,
    #and a flag indicating completion
    username = models.CharField(max_length=40)
    title    = models.CharField(max_length=40)
    due_date = models.DateTimeField(max_length=40)
    details  = models.CharField(max_length=140)
    is_completed = models.BooleanField()

    #returns a string with the relevant task information for debugging
    def __str__(self):
        if self.is_completed:
            completed = 'completed'
        else:
            completed = 'not completed'
        return datetime.strftime(self.due_date,'%m/%d/%Y %H:%M') + ' ' + self.title + ' ' + self.details + ' '  + comleted +'<br>'
