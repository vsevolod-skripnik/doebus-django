import pytest

from examples.services import DefaultGrouper

pytestmark = [pytest.mark.django_db]


def test_default_grouper(person_adam, pet_adams_cat, pet_adams_parrot):
    default_grouper = DefaultGrouper()

    rows = default_grouper()

    assert rows[0][0] == 2
    assert rows[0][1] == person_adam.id
