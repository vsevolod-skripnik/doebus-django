from django.db import models

from app.base.models import BaseModel


class Order(BaseModel):
    products = models.ManyToManyField(
        'products.Product',
        related_name='orders',
    )
