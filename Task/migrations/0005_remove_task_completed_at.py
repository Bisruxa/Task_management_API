# Generated by Django 5.1.4 on 2024-12-17 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0004_task_completed_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed_at',
        ),
    ]
