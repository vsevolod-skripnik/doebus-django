import pytest

from orders.models import Order


@pytest.fixture
def order(factory) -> Order:
    return factory.order()
