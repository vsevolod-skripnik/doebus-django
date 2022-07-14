from django.db import transaction
from django.db.models import F
from rest_framework.exceptions import ValidationError

from app.base.services import BaseService
from products.models import Product


class OrderBuyer(BaseService):
    def __init__(self, order):
        self.order = order
        self.order_items = self.order.items.all()

        products = Product.objects \
            .filter(order_items__order=self.order) \
            .select_for_update()
        self.products = {
            product.id: product
            for product in products
        }

    def validate_product_count(self):
        for order_item in self.order_items:
            product = self.products[order_item.product.id]

            if product.count < order_item.amount:
                raise ValidationError()

    @transaction.atomic
    def act(self):
        self.subtract_product_count()
        self.set_order_status()
        self.order.save()
        return self.order

    def subtract_product_count(self):
        for order_item in self.order_items:
            product = self.products[order_item.product.id]
            product.count -= order_item.amount
            product.save()

    def set_order_status(self):
        self.order.status = 'BOUGHT'
