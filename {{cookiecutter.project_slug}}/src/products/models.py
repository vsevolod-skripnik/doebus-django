from django.db import models

from app.base.models import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=255)
    cost = models.DecimalField(
        decimal_places=2,
        max_digits=10,
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
    )
    count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title}'
