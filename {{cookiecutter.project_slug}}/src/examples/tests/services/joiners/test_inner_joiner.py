import pytest

from examples.services import InnerJoiner

pytestmark = [pytest.mark.django_db]


def test_inner_joiner_inner_intersection(pet_adams_cat, pet_bobs_dog):
    inner_joiner = InnerJoiner()

    pets = inner_joiner()

    assert pets[0].owner_name == 'Adam'
    assert pets[1].owner_name == 'Bob'


def test_inner_joiner_left_table_missing(pet_without_owner):
    inner_joiner = InnerJoiner()

    pets = inner_joiner.act()

    assert pet_without_owner not in pets


def test_inner_joiner_right_table_missing(person_carl):
    inner_joiner = InnerJoiner()

    pets = inner_joiner()

    assert 'Carl' not in [pet.owner_name for pet in pets]
