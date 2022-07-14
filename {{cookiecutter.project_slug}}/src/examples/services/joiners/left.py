from django.db.models.query import RawQuerySet

from app.base.services import BaseService
from examples.models import Pet


class LeftJoiner(BaseService):
    """
    Left join (also called left outer join) selects rows,
    which are present in the left table (FROM),
    and the matching rows in the right table (JOIN)
    """

    QUERY = """
        SELECT
            examples_pet.id,
            examples_person.id,
            examples_person.name AS owner_name
        FROM examples_pet
        LEFT JOIN examples_person ON examples_pet.owner_id = examples_person.id;
    """

    def act(self) -> RawQuerySet:
        return Pet.objects.raw(self.QUERY)
