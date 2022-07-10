import pytest

from examples.models import Person
from examples.models import Pet


@pytest.fixture
def person_adam():
    return Person.objects.create(name='Adam')


@pytest.fixture
def person_bob():
    return Person.objects.create(name='Bob')


@pytest.fixture
def person_carl():
    return Person.objects.create(name='Carl')


@pytest.fixture
def pet_adams_cat(person_adam):
    return Pet.objects.create(name='Cat', owner=person_adam)


@pytest.fixture
def pet_adams_parrot(person_adam):
    return Pet.objects.create(name='Parrot', owner=person_adam)


@pytest.fixture
def pet_bobs_dog(person_bob):
    return Pet.objects.create(name='Dog', owner=person_bob)


@pytest.fixture
def pet_without_owner():
    return Pet.objects.create(name='Capybara')
