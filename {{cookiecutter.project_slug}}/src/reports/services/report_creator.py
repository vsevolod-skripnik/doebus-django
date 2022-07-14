from app.base.services import BaseService
from reports.models import Report


class ReportCreator(BaseService):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def create_report(self) -> Report:
        defaults = {**self.kwargs}
        return Report.objects.create(**defaults)

    def call_report_generator(self, report):
        from reports.tasks import generate_report
        generate_report.delay(report.id)

    def act(self):
        report = self.create_report()
        self.call_report_generator(report)
        return report
