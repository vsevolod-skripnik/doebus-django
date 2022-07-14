from decimal import Decimal
import pytest

from products.models import Product


@pytest.fixture
def product(factory) -> Product:
    return factory.product(
        title='The Holy Hand Grenade',
        cost=Decimal('21.99'),
        price=Decimal('42.99'),
        count=20,
    )
