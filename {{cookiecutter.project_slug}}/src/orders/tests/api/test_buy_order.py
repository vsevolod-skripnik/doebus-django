import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def order_buyer(mocker, order):
    return mocker.patch(
        'orders.services.OrderBuyer.__call__',
        return_value=order,
    )


def test_buy_order_call_order_buyer(as_user, order, order_buyer):
    as_user.post(f'/api/v1/orders/{order.id}/buy/')

    assert order_buyer.called_once()


def test_buy_order_response(as_user, order):
    got = as_user.post(f'/api/v1/orders/{order.id}/buy/')

    assert got['status'] == 'BOUGHT'
