from rest_framework.routers import SimpleRouter

from django.urls import include
from django.urls import path

from products.api import viewsets

router = SimpleRouter()
router.register('', viewsets.ProductViewSet)

app_name = 'products'
urlpatterns = [
    path('', include(router.urls)),
]
