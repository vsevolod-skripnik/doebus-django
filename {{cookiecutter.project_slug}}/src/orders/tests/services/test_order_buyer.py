import pytest

from orders.services import OrderBuyer

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def order_item(factory, product, order):
    return factory.order_item(
        order=order,
        product=product,
        amount=1,
    )


def test_order_buyer_set_order_status_bought(order):
    order_buyer = OrderBuyer(order)

    order_buyer.set_order_status()

    assert order_buyer.order.status == 'BOUGHT'


def test_order_buyer_save_order(order):
    order_buyer = OrderBuyer(order)

    order_buyer()

    order.refresh_from_db()
    assert order.status == 'BOUGHT'


def test_order_buyer_subtract_product_count(product, order, order_item):
    order_buyer = OrderBuyer(order)

    order_buyer.subtract_product_count()

    product.refresh_from_db()
    assert product.count == 19
