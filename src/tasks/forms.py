from django import forms
from django.forms import ModelForm
from .data import TASK_STATUS
from .models import Task


class TaskForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    #    self.fields['status'].widget.attrs['class'] = 'form-control form-select'
    #    self.fields['due_dt'].widget.attrs['class'] = 'form-control'
    #    self.fields['created_at'].widget.attrs['class'] = 'form-control dark'
        self.fields['created_at'].widget.attrs['readonly'] = True
    #    self.fields['person'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            "desc_text": forms.Textarea(attrs={'cols': 20, 'rows': 10}),
            "due_dt": forms.DateInput(attrs={'type': 'datetime-local'}),
        }
