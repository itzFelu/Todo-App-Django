# Generated by Django 4.2.14 on 2024-07-19 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_tasks_datetime_alter_tasks_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 19, 19, 6, 56, 457449)),
        ),
    ]
