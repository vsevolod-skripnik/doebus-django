from rest_framework.routers import SimpleRouter

from django.urls import include
from django.urls import path

from orders.api import viewsets

router = SimpleRouter()
router.register('', viewsets.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
