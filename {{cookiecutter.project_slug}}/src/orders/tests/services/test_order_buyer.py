import pytest

from orders.services import OrderBuyer

pytestmark = [pytest.mark.django_db]


def test_order_buyer_set_order_status_bought(order):
    order_buyer = OrderBuyer(order)

    order_buyer.set_order_status()

    assert order_buyer.order.status == 'BOUGHT'


def test_order_buyer_save_order(order):
    order_buyer = OrderBuyer(order)

    order_buyer()

    order.refresh_from_db()
    assert order.status == 'BOUGHT'
