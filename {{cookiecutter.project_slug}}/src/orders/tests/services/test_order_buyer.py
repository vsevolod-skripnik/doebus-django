import pytest

from rest_framework.exceptions import ValidationError

from orders.services import OrderBuyer

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def order_item(factory, product, order):
    return factory.order_item(
        order=order,
        product=product,
        amount=1,
    )


@pytest.fixture
def order_item_full_amount(factory, product, order):
    return factory.order_item(
        order=order,
        product=product,
        amount=20,
    )


@pytest.fixture
def order_item_overflowing_amount(factory, product, order):
    return factory.order_item(
        order=order,
        product=product,
        amount=21,
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


def test_order_buyer_if_full_amount(product, order, order_item_full_amount):
    order_buyer = OrderBuyer(order)

    order_buyer()

    product.refresh_from_db()
    assert product.count == 0


def test_order_buyer_validate_product_count_if_full_amount(product, order, order_item_full_amount):
    order_buyer = OrderBuyer(order)

    order_buyer.validate_product_count()


def test_order_buyer_validate_product_count_if_overflowing_amount(product, order, order_item_overflowing_amount):
    order_buyer = OrderBuyer(order)

    with pytest.raises(ValidationError):
        order_buyer.validate_product_count()
