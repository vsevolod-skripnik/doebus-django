from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.base.api.viewsets import BaseModelViewSet
from products.api import serializers
from products.models import Product


class ProductViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.order_by('-id')
    serializer_action_classes = {
        'create': serializers.ProductCreateSerializer,
        'update': serializers.ProductUpdateSerializer,
        'partial_update': serializers.ProductUpdateSerializer,
    }
