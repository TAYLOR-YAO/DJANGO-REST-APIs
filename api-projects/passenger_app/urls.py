from django.urls import path
from passenger_app import views
urlpatterns = [
    path('', views.passenger_list),
    path('<int:pk>', views.passenger_details),

]
