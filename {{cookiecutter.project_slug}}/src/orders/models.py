from django.db import models

from app.base.models import BaseModel


class OrderItem(BaseModel):
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        related_name='items',
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='order_items',
    )

    amount = models.PositiveIntegerField()


class Order(BaseModel):
    status = models.CharField(
        max_length=255,
        default='CREATED',
    )
