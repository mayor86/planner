# Generated by Django 4.2.5 on 2023-09-24 12:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_created_at_alter_task_due_dt_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_dt',
            field=models.DateTimeField(null=True, verbose_name='Сделать до'),
        ),
        migrations.AlterField(
            model_name='task',
            name='person',
            field=models.CharField(max_length=100, null=True, verbose_name='Участник'),
        ),
    ]
