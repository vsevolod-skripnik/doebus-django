import pytest

from examples.services import RightJoiner

pytestmark = [pytest.mark.django_db]


def test_right_joiner_inner_intersection(pet_adams_cat, pet_bobs_dog):
    right_joiner = RightJoiner()

    pets = right_joiner()

    assert pets[0].owner_name == 'Adam'
    assert pets[1].owner_name == 'Bob'


def test_right_joiner_left_table_missing(pet_without_owner):
    right_joiner = RightJoiner()

    pets = right_joiner.act()

    assert pet_without_owner not in pets


def test_right_joiner_right_table_null(person_carl):
    right_joiner = RightJoiner()

    pets = right_joiner()

    assert pets[0].id is None
    assert pets[0].owner_name == 'Carl'
