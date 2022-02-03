from django.urls import path, include
from cbvserializers_app import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('', views.StudentViewSet)
urlpatterns = [
    path('', include(router.urls)),

]
