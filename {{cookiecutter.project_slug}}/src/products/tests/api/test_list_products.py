import pytest

pytestmark = [pytest.mark.django_db]


def test_list_products(as_user, product):
    got = as_user.get('/api/v1/products/')

    assert got['results'][0]['title'] == 'The Holy Hand Grenade'
    assert got['results'][0]['cost'] == 21.99
    assert got['results'][0]['price'] == 42.99
    assert got['results'][0]['count'] == 20
