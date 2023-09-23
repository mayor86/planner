from django.urls import path
from .views import TaskUpdateView, TaskIndexView

app_name = 'tasks'

urlpatterns = [
    path('', TaskIndexView.as_view(), name='index'),
    path('update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
]