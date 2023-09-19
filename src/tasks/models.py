from django.db import models
from .data import TASK_STATUS
from datetime import datetime

class Task(models.Model):
    """Задачи"""
    desc_text = models.TextField('Описание задачи', max_length=255)
    status = models.CharField('Статус', max_length=30, choices=TASK_STATUS, default='Нужно сделать')
    created_at = models.DateField('Дата создания', blank=True, null=True)
    due_dt = models.DateField('Сделать до', blank=True, null=True)
    person = models.CharField('Участник', blank=True, null=True, max_length=100)

    class Meta:
        db_table = 'task'