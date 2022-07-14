from django.db import models

from app.base.models import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=255)
    cost = models.FloatField()
    price = models.FloatField()
    count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title}'
