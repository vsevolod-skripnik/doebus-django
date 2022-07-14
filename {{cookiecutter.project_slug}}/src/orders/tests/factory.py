from typing import Dict

from app.base.testing import register
from orders.models import Order


@register
def order(self, **kwargs: Dict) -> Order:
    return self.mixer.blend('orders.Order', **kwargs)
