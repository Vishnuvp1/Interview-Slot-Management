# Generated by Django 4.0.2 on 2022-02-15 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='end_datetime',
            field=models.CharField(default=datetime.datetime.now, max_length=180),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='start_datetime',
            field=models.CharField(default=datetime.datetime.now, max_length=180),
        ),
    ]
