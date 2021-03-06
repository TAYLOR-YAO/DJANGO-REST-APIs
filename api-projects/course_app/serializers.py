from django.db import models
from django.db.models import fields
from rest_framework import serializers
from course_app.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'descriptions', 'ratings']
