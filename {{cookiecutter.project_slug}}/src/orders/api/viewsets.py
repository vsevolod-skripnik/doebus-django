from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.base.api.viewsets import BaseModelViewSet
from orders.api import serializers
from orders.models import Order
from orders.services import OrderBuyer


class OrderViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()
    serializer_action_classes = {
        'create': serializers.OrderCreateSerializer,
    }

    @action(detail=True, methods=['POST'])
    def buy(self, *args, **kwargs):
        order = self.get_object()
        order_buyer = OrderBuyer(order)
        order = order_buyer()
        return self.response(order, 201)
