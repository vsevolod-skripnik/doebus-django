from app.base.services import BaseService
from reports.models import Report


class ReportCreator(BaseService):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def create_report(self) -> Report:
        defaults = {**self.kwargs}
        return Report.objects.create(**defaults)

    def act(self):
        return self.create_report()
