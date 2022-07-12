from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.base.api.viewsets import BaseModelViewSet
from orders.api import serializers
from orders.models import Order


class OrderViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()
    serializer_action_classes = {}
