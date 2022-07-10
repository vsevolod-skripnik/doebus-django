import pytest

from examples.services import HavingGrouper

pytestmark = [pytest.mark.django_db]


def test_having_grouper_if_2_pets(person_adam, pet_adams_cat, pet_adams_parrot):
    having_grouper = HavingGrouper()

    rows = having_grouper()

    assert rows[0][0] == 2
    assert rows[0][1] == person_adam.id


def test_having_grouper_if_1_pet(pet_adams_cat):
    having_grouper = HavingGrouper()

    rows = having_grouper()

    assert rows == []
