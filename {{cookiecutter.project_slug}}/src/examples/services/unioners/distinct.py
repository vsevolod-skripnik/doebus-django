from django.db.models.query import RawQuerySet

from app.services import BaseService
from examples.models import Pet


class DistinctUnioner(BaseService):
    """
    Union statement combines results of two SELECT statements,
    filtering out duplicate rows by default
    """

    QUERY = """
        SELECT * FROM examples_pet
        UNION
        SELECT * FROM examples_pet
    """

    def act(self) -> RawQuerySet:
        return Pet.objects.raw(self.QUERY)
