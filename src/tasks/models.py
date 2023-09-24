from django.db import models
from django.utils import timezone
from .data import TASK_STATUS


class Task(models.Model):
    """Задачи"""
    desc_text = models.CharField('Описание задачи', max_length=255)
    status = models.CharField('Статус', max_length=30, choices=TASK_STATUS, default='Нужно сделать')
    created_at = models.DateTimeField('Дата создания', default=timezone.now)
    due_dt = models.DateTimeField('Сделать до', null=True, blank=True,)
    person = models.CharField('Участник', null=True, blank=True, max_length=100, default='')

    class Meta:
        db_table = 'task'
        ordering = ['-created_at']
