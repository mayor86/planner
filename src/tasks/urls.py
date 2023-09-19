from django.urls import path
from .views import tasks_index

app_name = 'tasks'

urlpatterns = [
    path('', tasks_index, name='index'),
]