from django import forms

#Form for the task info
class TaskForm(forms.Form):
    title = forms.CharField(label='Task Title', max_length=40, required=True)
    due_date = forms.DateTimeField(
            required = True,
            input_formats = ['%m/%d/%Y %H:%M'],
            widget = forms.DateTimeInput(
                attrs = {
                    'type': 'datetime-local',
                    'class': 'form-control'},
                format = '%m/%d/%Y %H:%M'))
    details = forms.CharField(
            required = True,
            max_length = 140,
            widget = forms.Textarea(attrs={'placeholder': 'Details'}))

