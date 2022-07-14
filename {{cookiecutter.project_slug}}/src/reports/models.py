from django.db import models

from app.base.models import BaseModel


class Report(BaseModel):
    status = models.CharField(
        default='CREATED',
        max_length=255,
    )
    data = models.JSONField(
        default=dict,
    )
