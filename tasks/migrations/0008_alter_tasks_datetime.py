# Generated by Django 4.2.14 on 2024-07-19 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_tasks_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 19, 19, 8, 17, 271387)),
        ),
    ]
