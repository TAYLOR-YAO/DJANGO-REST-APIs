from django.shortcuts import render
from course_app.serializers import CourseSerializer
from course_app.models import Course

# ---------------------------# using mixins views example------------------------------------------------------------------
from rest_framework import generics


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
