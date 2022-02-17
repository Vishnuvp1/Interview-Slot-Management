from urllib import response
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveAPIView, \
    GenericAPIView, DestroyAPIView, ListAPIView, CreateAPIView

from .serializers import CandidateTimeSlotSerializer, InterviewerTimeSlotSerializer
from InterviewApp.models import CandidateTimeSlot, InterviewerTimeSlot
from EntriInterview import api_exception_handling as error
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status, serializers
import datetime


class CandidateTimeSlotView(CreateAPIView, UpdateAPIView):

    serializer_class = CandidateTimeSlotSerializer

    def post(self, request, *args, **kwargs):
        candidate_id = request.data.get('candidate_id', None)
        if candidate_id:
            try:
                candidate_instance = CandidateTimeSlot.objects.get(
                    id=candidate_id)
            except ObjectDoesNotExist:
                raise error.ValidationError("Candidate Not Found!", 400)

            serializer = self.get_serializer(
                candidate_instance, data=self.request.data)
        else:
            serializer = self.get_serializer(data=self.request.data)

        try:
            serializer.is_valid(raise_exception=True)
            if candidate_id:
                self.perform_update(serializer)
                response = Response(
                    {"message": "Candidate timeslot updated."}, status=status.HTTP_200_OK)

            else:
                serializer.save()
                response = Response({"message": "Candidate timeslot created successfully."},
                                    status=status.HTTP_201_CREATED)
            return response

        except Exception as e:

            raise error.ValidationError(*(str(e), 400))


class InterviewerTimeSlotView(CreateAPIView, UpdateAPIView):

    serializer_class = InterviewerTimeSlotSerializer

    def post(self, request, *args, **kwargs):
        candidate_id = request.data.get('candidate_id', None)
        if candidate_id:
            try:
                candidate_instance = InterviewerTimeSlot.objects.get(
                    id=candidate_id)
            except ObjectDoesNotExist:
                raise error.ValidationError("Interviewer Not Found!", 400)

            serializer = self.get_serializer(
                candidate_instance, data=self.request.data)
        else:
            serializer = self.get_serializer(data=self.request.data)

        try:
            serializer.is_valid(raise_exception=True)
            if candidate_id:
                self.perform_update(serializer)
                response = Response(
                    {"message": "Interviewer timeslot updated."}, status=status.HTTP_200_OK)

            else:
                serializer.save()
                response = Response({"message": "Candidate timeslot created successfully."},
                                    status=status.HTTP_201_CREATED)
            return response

        except Exception as e:

            raise error.ValidationError(*(str(e), 400))


class AvailableTimeSlotes(RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        candidate_id = request.query_params.get('candidate_id', None)

        interviewer_id = request.query_params.get('interviewer_id', None)
        print(interviewer_id)

        if not CandidateTimeSlot.objects.filter(id=candidate_id).exists():
            raise error.ValidationError("Candidate not Found!", 400)

        if not InterviewerTimeSlot.objects.filter(id=candidate_id).exists():
            raise error.ValidationError("Interviewer not Found!", 400)

        try:
            candidate_instance = CandidateTimeSlot.objects.get(id=candidate_id)
            interviewer_instance = InterviewerTimeSlot.objects.get(
                id=interviewer_id)

            candidate_start_time = candidate_instance.start_datetime
            candidate_end_time = candidate_instance.end_datetime
            interviewer_start_time = interviewer_instance.start_datetime
            interviewer_end_time = interviewer_instance.end_datetime

            if candidate_start_time.date() != interviewer_start_time.date():
                raise error.ValidationError(
                    "Date is not matching for the candidate and interviewer. ", 400)

            if candidate_start_time < interviewer_start_time:
                start_time = interviewer_start_time.strftime("%H:%M")
            else:
                start_time = candidate_start_time.strftime("%H:%M")

            if candidate_end_time < interviewer_end_time:
                end_time = candidate_end_time.strftime("%H:%M")
            else:
                end_time = interviewer_end_time.strftime("%H:%M")

            timeslot = []
            time = datetime.datetime.strptime(start_time, "%H:%M")
            end = datetime.datetime.strptime(end_time, "%H:%M")

            while time < end:
                start_time = time.strftime("%H:%M")
                time += datetime.timedelta(hours=1)
                end_time = time.strftime("%H:%M")
                timeslot.append(
                    {"start_time": start_time, "end_time": end_time})

            data = {
                "candidate_name": candidate_instance.candidate_name,
                "interviewer_name": interviewer_instance.interviewer_name,
                "timeslot": timeslot,
            }

            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            raise error.ValidationError(*(str(e), 400))
