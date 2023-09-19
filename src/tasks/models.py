from django.db import models

class Task(models.Model):
    """Задачи"""
    desc_text = models.CharField('Описание задачи', max_length=255)
    status = models.CharField('Статус', max_length=30)

    class Meta:
        db_table = 'task'