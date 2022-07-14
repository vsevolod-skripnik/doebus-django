from typing import Dict

from app.base.testing import register
from reports.models import Report


@register
def report(self, **kwargs: Dict) -> Report:
    return self.mixer.blend('reports.Report', **kwargs)
