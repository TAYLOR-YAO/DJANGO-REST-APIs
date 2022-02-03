from django.urls import path
from students_app import views
urlpatterns = [
    path('', views.student_list),
    path('<int:pk>', views.student_details),

]
