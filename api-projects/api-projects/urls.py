from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees/', include('employees_app.urls')),
    path('api/students/', include('students_app.urls')),
    path('api/passengers/', include('passenger_app.urls')),
    path('api/cbvserializers/students/', include('cbvserializers_app.urls')),
    path('api/courses/', include('course_app.urls')),
    path('api/authbook/', include('nested_serializer_app.urls')),
    path('api/costomerorders/', include('nested_serializer_phone_app.urls')),

]
