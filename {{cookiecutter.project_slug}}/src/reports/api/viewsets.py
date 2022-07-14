from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.base.api.viewsets import BaseModelViewSet
from reports.api import serializers
from reports.models import Report
from reports.services import ReportCreator


class ReportViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serializers.ReportSerializer
    queryset = Report.objects.order_by('-id')
    serializer_action_classes = {
        'create': serializers.ReportCreateSerializer,
    }

    def perform_create(self, serializer):
        report_creator = ReportCreator(
            **serializer.validated_data,
        )
        return report_creator()
