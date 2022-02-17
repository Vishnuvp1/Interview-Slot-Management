from django.urls import path
from . import views


urlpatterns = [
    path('candidate_timeslot/', views.CandidateTimeSlotView.as_view(), name='candidate_timeslot'),
    path('interviewer_timeslot/', views.InterviewerTimeSlotView.as_view(), name='interviewer_timeslot'),
    path('available_timeslots/', views.AvailableTimeSlotes.as_view(), name='available_timeslots'),

]