# Generated by Django 4.2.5 on 2023-09-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_task_options_alter_task_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_dt',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Сделать до'),
        ),
        migrations.AlterField(
            model_name='task',
            name='person',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Участник'),
        ),
    ]
