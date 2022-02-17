# Generated by Django 4.0.2 on 2022-02-15 11:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('end_datetime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateTimeSlot',
            fields=[
                ('timeslot_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='InterviewApp.timeslot')),
                ('candidate_name', models.CharField(blank=True, max_length=180, null=True)),
            ],
            bases=('InterviewApp.timeslot',),
        ),
        migrations.CreateModel(
            name='InterviewerTimeSlot',
            fields=[
                ('timeslot_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='InterviewApp.timeslot')),
                ('interviewer_name', models.CharField(blank=True, max_length=180, null=True)),
            ],
            bases=('InterviewApp.timeslot',),
        ),
    ]