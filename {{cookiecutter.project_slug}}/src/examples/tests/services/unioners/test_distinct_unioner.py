import pytest

from examples.services import DistinctUnioner

pytestmark = [pytest.mark.django_db]


def test_distinct_unioner(pet_adams_cat):
    distinct_unioner = DistinctUnioner()

    pets = distinct_unioner()

    assert len(pets) == 1
    assert pets[0].name == 'Cat'
