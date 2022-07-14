from django.db import transaction
from django.db.models import F

from app.base.services import BaseService
from products.models import Product


class OrderBuyer(BaseService):
    def __init__(self, order):
        self.order = order

    @transaction.atomic
    def act(self):
        self.subtract_product_count()
        self.set_order_status()
        self.order.save()
        return self.order

    def subtract_product_count(self):
        for order_item in self.order.items.all():
            Product.objects \
                .filter(id=order_item.product.id) \
                .update(count=F('count') - order_item.amount)

    def set_order_status(self):
        self.order.status = 'BOUGHT'
