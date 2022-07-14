import pytest

from orders.models import Order

pytestmark = [pytest.mark.django_db]


def test_create_order_instance(as_user):
    as_user.post('/api/v1/orders/')

    order = Order.objects.last()
    assert order.status == 'CREATED'


def test_create_order_response(as_user, product):
    got = as_user.post('/api/v1/orders/')

    assert got['id']
    assert got['status'] == 'CREATED'
