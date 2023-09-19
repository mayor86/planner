from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = 'id', 'created_at', 'desc_text', 'status', 'due_dt', 'person'


admin.site.register(Task, TaskAdmin)
