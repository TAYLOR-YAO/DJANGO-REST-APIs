from django.shortcuts import render
from django.http import JsonResponse
from employees_app.models import Employee


def employees_view(request):
    data = Employee.objects.all()
    response = {'employees': list(data.values('id', 'name', 'salary'))}
    return JsonResponse(response)
