from django.urls import path, include
from nested_serializer_phone_app import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet)
urlpatterns = [
    path('', include(router.urls)),

]
