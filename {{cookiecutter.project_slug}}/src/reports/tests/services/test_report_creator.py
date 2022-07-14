import pytest

from reports.services import ReportCreator

pytestmark = [pytest.mark.django_db]


def test_report_creator():
    report_generator = ReportCreator()

    report = report_generator()

    assert report.status == 'CREATED'
