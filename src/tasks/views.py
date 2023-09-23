from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.views import View
from .forms import TaskForm
from .models import Task


class TaskIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = TaskForm()
        context = {
            'form': form,
            "tasks": Task.objects.all(),
        }
        return render(request, 'tasks/tasks_index.html', context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(request.path)


class TaskUpdateView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        task_instance = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task_instance)
        print(task_instance)
        context = {
            'form': form
        }

        return render(request, 'tasks/tasks_update_form.html', context=context)

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        task_instance = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task_instance)
        if form.is_valid():
            form.save()
            url = reverse('tasks:index')

            return redirect(url)


def tasks_create(request) -> HttpResponse:
    """Создать новую задачу"""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse('tasks:index')
            return redirect(url)
    else:
        form = TaskForm()

    context = {
        'form': form
    }

    return render(request, 'tasks/tasks_update_form.html', context=context)