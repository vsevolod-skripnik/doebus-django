import pytest

from examples.services import SelfJoiner

pytestmark = [pytest.mark.django_db]


def test_self_joiner(pet_adams_cat, pet_adams_parrot):
    self_joiner = SelfJoiner()

    pets = self_joiner()

    assert pets[0].name == 'Cat'
    assert pets[0].self_name == 'Cat'
    assert pets[0].another_name == 'Parrot'
    assert pets[1].name == 'Parrot'
    assert pets[1].self_name == 'Parrot'
    assert pets[1].another_name == 'Cat'
