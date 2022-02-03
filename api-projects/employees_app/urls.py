from django.urls import path
from employees_app import views
urlpatterns = [
    path('', views.employees_view),
]
