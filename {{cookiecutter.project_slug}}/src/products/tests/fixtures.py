import pytest

from products.models import Product


@pytest.fixture
def product(factory) -> Product:
    return factory.product(
        title='The Holy Hand Grenade',
        cost=21.99,
        price=42.99,
        count=20,
    )
