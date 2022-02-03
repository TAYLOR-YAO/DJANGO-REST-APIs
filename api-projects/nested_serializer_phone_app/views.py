from nested_serializer_phone_app.serializers import OrderSerializer, CustomerSerializer
from nested_serializer_phone_app.models import Customer, Order
# ------------------------------------using generics views example-----------------------
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
