from typing import Dict

from app.base.testing import register
from app.base.testing.types import FactoryProtocol
from products.models import Product


@register
def product(self: FactoryProtocol, **kwargs: Dict) -> Product:
    return self.mixer.blend('products.Product', **kwargs)
