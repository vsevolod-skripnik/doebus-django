import pytest

from examples.services import AllUnioner

pytestmark = [pytest.mark.django_db]


def test_all_unioner(pet_adams_cat):
    all_unioner = AllUnioner()

    pets = all_unioner()

    assert pets[0].name == 'Cat'
    assert pets[1].name == 'Cat'
