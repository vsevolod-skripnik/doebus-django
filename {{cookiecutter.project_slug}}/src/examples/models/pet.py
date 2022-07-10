from django.db import models

from app.models import DefaultModel


class Pet(DefaultModel):
    name = models.CharField(max_length=255)

    owner = models.ForeignKey(
        'examples.Person',
        on_delete=models.CASCADE,
        related_name='pets',
        null=True,
    )
