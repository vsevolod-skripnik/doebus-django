import pytest

from reports.models import Report

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def report_creator(mocker, report):
    return mocker.patch(
        'reports.services.ReportCreator.__call__',
        return_value=report,
    )


def test_create_report_instance(as_user):
    as_user.post('/api/v1/reports/')

    report = Report.objects.last()
    assert report.id
    assert report.status == 'CREATED'


def test_create_report_response(as_user):
    got = as_user.post('/api/v1/reports/')

    assert got['id']
    assert got['status'] == 'CREATED'


def test_create_report_call_report_creator(as_user, report_creator):
    as_user.post('/api/v1/reports/')

    assert report_creator.called_once()
