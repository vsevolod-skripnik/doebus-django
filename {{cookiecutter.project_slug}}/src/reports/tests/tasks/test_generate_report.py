import pytest

from reports.tasks import generate_report

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def report_generator(mocker):
    return mocker.patch('reports.services.ReportGenerator.__call__')


def test_generate_report_call_report_generator(report, report_generator):
    generate_report.delay(report.id)

    report_generator.assert_called_once()
