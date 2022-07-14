import pytest

from products.models import Product

pytestmark = [pytest.mark.django_db]


def test_create_product_instance(as_user):
    as_user.post('/api/v1/products/', {
        'title': 'MacBook Pro',
        'cost': 1299.0,
        'price': 2499.0,
        'count': 10,
    })

    product = Product.objects.last()
    assert product.title == 'MacBook Pro'
    assert product.cost == 1299.0
    assert product.price == 2499.0
    assert product.count == 10


def test_create_product_response(as_user):
    got = as_user.post('/api/v1/products/', {
        'title': 'MacBook Pro',
        'cost': 1299.0,
        'price': 2499.0,
        'count': 10,
    })

    assert got['title'] == 'MacBook Pro'
    assert got['cost'] == 1299.0
    assert got['price'] == 2499.0
    assert got['count'] == 10
