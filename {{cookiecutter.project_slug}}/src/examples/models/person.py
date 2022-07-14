from django.db import models

from app.base.models import BaseModel


class Person(BaseModel):
    name = models.CharField(max_length=255)
