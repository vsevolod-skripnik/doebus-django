from django.db import models

from app.base.models import BaseModel


class Pet(BaseModel):
    name = models.CharField(max_length=255)

    owner = models.ForeignKey(
        'examples.Person',
        on_delete=models.CASCADE,
        related_name='pets',
        null=True,
    )
