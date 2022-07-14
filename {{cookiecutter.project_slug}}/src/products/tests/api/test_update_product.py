from decimal import Decimal
import pytest

pytestmark = [pytest.mark.django_db]


def test_update_product_instance(as_user, product):
    as_user.patch(f'/api/v1/products/{product.id}/', {
        'cost': 1299.99,
        'price': 2499.99,
        'count': 10,
    })

    product.refresh_from_db()
    assert product.cost == Decimal('1299.99')
    assert product.price == Decimal('2499.99')
    assert product.count == 10


def test_update_product_response(as_user, product):
    got = as_user.patch(f'/api/v1/products/{product.id}/', {
        'cost': 1299.99,
        'price': 2499.99,
        'count': 10,
    })

    assert got['cost'] == 1299.99
    assert got['price'] == 2499.99
    assert got['count'] == 10
