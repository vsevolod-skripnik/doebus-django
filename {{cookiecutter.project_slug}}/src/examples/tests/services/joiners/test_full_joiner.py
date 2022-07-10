import pytest

from examples.services import FullJoiner

pytestmark = [pytest.mark.django_db]


def test_full_joiner_full_intersection(pet_adams_cat, pet_bobs_dog):
    full_joiner = FullJoiner()

    pets = full_joiner()

    assert pets[0].owner_name == 'Adam'
    assert pets[1].owner_name == 'Bob'


def test_full_joiner_left_table_null(pet_without_owner):
    full_joiner = FullJoiner()

    pets = full_joiner.act()

    assert pets[0].id is not None
    assert pets[0].owner_name is None


def test_full_joiner_right_table_null(person_carl):
    full_joiner = FullJoiner()

    pets = full_joiner()

    assert pets[0].id is None
    assert pets[0].owner_name == 'Carl'
