from django.db import models
from django.db.models import fields
from rest_framework import serializers
from passenger_app.models import Passenger


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'firstName', 'lastName', 'rewardPoint']
