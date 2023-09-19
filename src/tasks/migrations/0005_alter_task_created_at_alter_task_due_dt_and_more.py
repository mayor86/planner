# Generated by Django 4.2.5 on 2023-09-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_created_at_task_due_dt_task_person_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(blank=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_dt',
            field=models.DateField(blank=True, null=True, verbose_name='Сделать до'),
        ),
        migrations.AlterField(
            model_name='task',
            name='person',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Участник'),
        ),
    ]
