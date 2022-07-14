from typing import Dict

from app.base.testing import register
from orders.models import Order
from orders.models import OrderItem


@register
def order(self, **kwargs: Dict) -> Order:
    return self.mixer.blend('orders.Order', **kwargs)


@register
def order_item(self, **kwargs: Dict) -> OrderItem:
    return self.mixer.blend('orders.OrderItem', **kwargs)
