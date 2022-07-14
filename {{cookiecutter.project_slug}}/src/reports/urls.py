from rest_framework.routers import SimpleRouter

from django.urls import include
from django.urls import path

from reports.api import viewsets

router = SimpleRouter()
router.register('', viewsets.ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
