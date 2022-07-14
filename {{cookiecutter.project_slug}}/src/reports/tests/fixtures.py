import pytest

from reports.models import Report


@pytest.fixture
def report(factory) -> Report:
    return factory.report()
