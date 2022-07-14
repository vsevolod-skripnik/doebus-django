import pytest

from app.base.testing.factory import FixtureFactory


@pytest.fixture
def factory() -> FixtureFactory:
    return FixtureFactory()
