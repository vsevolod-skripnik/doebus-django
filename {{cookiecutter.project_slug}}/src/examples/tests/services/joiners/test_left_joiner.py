import pytest

from examples.services import LeftJoiner

pytestmark = [pytest.mark.django_db]


def test_left_joiner_inner_intersection(pet_adams_cat, pet_bobs_dog):
    left_joiner = LeftJoiner()

    pets = left_joiner()

    assert pets[0].owner_name == 'Adam'
    assert pets[1].owner_name == 'Bob'


def test_left_joiner_left_table_null(pet_without_owner):
    left_joiner = LeftJoiner()

    pets = left_joiner.act()

    assert pet_without_owner in pets
    assert pets[0].owner_name is None


def test_left_joiner_right_table_missing(person_carl):
    left_joiner = LeftJoiner()

    pets = left_joiner()

    assert 'Carl' not in [pet.owner_name for pet in pets]
