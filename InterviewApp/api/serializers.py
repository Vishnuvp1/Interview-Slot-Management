from rest_framework import serializers
from EntriInterview import api_exception_handling as error
from django.utils import timezone
from datetime import datetime
import pytz
from InterviewApp.models import CandidateTimeSlot, InterviewerTimeSlot

class CandidateTimeSlotSerializer(serializers.ModelSerializer):

    start_datetime = serializers.SerializerMethodField()
    end_datetime = serializers.SerializerMethodField()

    def get_start_datetime(self,instance):
        return instance.start_datetime.timestamp()

    def get_end_datetime(self,instance):
        return instance.end_datetime.timestamp()

    def validate(self,data):

        if not self.initial_data.get('candidate_name'):
            raise error.ValidationError("Candidates Name is required.", 400)

        start_datetime = self.initial_data.get('start_datetime', None)
        if not start_datetime:
            raise error.ValidationError("Start date and time is required.", 400)

        start_datetime = float(start_datetime)

        end_datetime = self.initial_data.get('end_datetime', None)
        if not end_datetime:
            raise error.ValidationError("End date and time is required.", 400)

        end_datetime = float(end_datetime)



        if start_datetime < timezone.now().timestamp():
            raise serializers.ValidationError({"message" : "Start time is lesser than current time. "})

        if start_datetime >= end_datetime:
            raise serializers.ValidationError({"message" : "End time is lesser than start Time ."})

        if end_datetime < timezone.now().timestamp():
            raise serializers.ValidationError({"message" : "End time is lesser than current time ."})


        start_datetime = datetime.fromtimestamp(float(start_datetime), tz=pytz.UTC)
        end_datetime = datetime.fromtimestamp(float(end_datetime), tz=pytz.UTC)

        if start_datetime.date() != end_datetime.date():
            raise error.ValidationError("Please select the same date for the available time slot.", 400)

        data['start_datetime'] = str(start_datetime)
        data['end_datetime'] = str(end_datetime)

        return data

    
    def create(self, validated_data):

        candidate_timeslot = CandidateTimeSlot.objects.create(
            candidate_name=validated_data['candidate_name'],
            start_datetime=validated_data['start_datetime'],
            end_datetime=validated_data['end_datetime'],
        )

        return candidate_timeslot


    class Meta:
        model = CandidateTimeSlot
        fields = ('candidate_name', 'start_datetime', 'end_datetime')


class InterviewerTimeSlotSerializer(serializers.ModelSerializer):

    start_datetime = serializers.SerializerMethodField()
    end_datetime = serializers.SerializerMethodField()

    def get_start_datetime(self,instance):
        return instance.start_datetime.timestamp()

    def get_end_datetime(self,instance):
        return instance.end_datetime.timestamp()

    def validate(self,data):

        if not self.initial_data.get('interviewer_name'):
            raise error.ValidationError("Interviewer Name is required.", 400)

        start_datetime = self.initial_data.get('start_datetime', None)
        if not start_datetime:
            raise error.ValidationError("Start date and time is required.", 400)

        start_datetime = float(start_datetime)

        end_datetime = self.initial_data.get('end_datetime', None)
        if not end_datetime:
            raise error.ValidationError("End date and time is required.", 400)

        end_datetime = float(end_datetime)



        if start_datetime < timezone.now().timestamp():
            raise serializers.ValidationError({"message" : "Start time is lesser than current time. "})

        if start_datetime >= end_datetime:
            raise serializers.ValidationError({"message" : "End time is lesser than start Time ."})

        if end_datetime < timezone.now().timestamp():
            raise serializers.ValidationError({"message" : "End time is lesser than current time ."})


        start_datetime = datetime.fromtimestamp(float(start_datetime), tz=pytz.UTC)
        end_datetime = datetime.fromtimestamp(float(end_datetime), tz=pytz.UTC)

        if start_datetime.date() != end_datetime.date():
            raise error.ValidationError("Please select the same date for the available time slot.", 400)

        data['start_datetime'] = str(start_datetime)
        data['end_datetime'] = str(end_datetime)

        return data

    
    def create(self, validated_data):

        interviewer_timeslot = InterviewerTimeSlot.objects.create(
            interviewer_name=validated_data['interviewer_name'],
            start_datetime=validated_data['start_datetime'],
            end_datetime=validated_data['end_datetime'],
        )

        return interviewer_timeslot


    class Meta:
        model = InterviewerTimeSlot
        fields = ('interviewer_name', 'start_datetime', 'end_datetime')