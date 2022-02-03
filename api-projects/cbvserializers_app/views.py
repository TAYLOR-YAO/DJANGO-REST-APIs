from django.shortcuts import render
from cbvserializers_app.serializers import StudentSerializer
from cbvserializers_app.models import Student
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters

# ------------------------------------using generics views example-----------------------
from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'score']
    ordering = ['id', 'score']  # default ordering
