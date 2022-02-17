from datetime import datetime

from django.db import models

# Create your models here.


class TimeSlot(models.Model):

    start_datetime = models.CharField(max_length=180,
        default=datetime.now, null=False, blank=False)
    end_datetime = models.CharField( max_length=180,
        default=datetime.now, null=False, blank=False)


class CandidateTimeSlot(TimeSlot):

    candidate_name = models.CharField(max_length=180, null=True, blank=True)

    def __str__(self):
        return self.candidate_name


class InterviewerTimeSlot(TimeSlot):

    interviewer_name = models.CharField(max_length=180, null=True, blank=True)

    def __str__(self):
        return self.interviewer_name
