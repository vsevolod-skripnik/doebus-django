from django.db.models.query import RawQuerySet

from app.services import BaseService
from examples.models import Pet


class AllUnioner(BaseService):
    """
    Union statement combines results of two SELECT statements,
    including duplicates if ALL keyword is present
    """

    QUERY = """
        SELECT * FROM examples_pet
        UNION ALL
        SELECT * FROM examples_pet
    """

    def act(self) -> RawQuerySet:
        return Pet.objects.raw(self.QUERY)
