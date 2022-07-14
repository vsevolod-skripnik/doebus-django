from app.celery import celery
from reports.models import Report
from reports.services import ReportGenerator


@celery.task(name='generate_report')
def generate_report(report_id: int):
    report = Report.objects.get(id=report_id)
    report_generator = ReportGenerator(report)
    report_generator()
