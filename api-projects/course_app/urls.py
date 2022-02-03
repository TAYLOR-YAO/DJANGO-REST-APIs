from django.urls import path
from course_app import views
urlpatterns = [
    path('', views.CourseList.as_view()),
    path('<int:pk>', views.CourseDetails.as_view()),

]
