from django.forms import ModelForm

from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = 'created_at', 'desc_text', 'status', 'due_dt', 'person'

        # widgets = {
        #     'created_at': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        #     'desc_text': forms.Textarea(attrs={'type': 'text', 'class': 'form-control'}),
        #     'status': forms.Textarea(attrs={'class': 'form-control'}),
        #     'due_dt': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        # }