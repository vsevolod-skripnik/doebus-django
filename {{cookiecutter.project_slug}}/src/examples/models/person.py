from django.db import models

from app.models import DefaultModel


class Person(DefaultModel):
    name = models.CharField(max_length=255)
