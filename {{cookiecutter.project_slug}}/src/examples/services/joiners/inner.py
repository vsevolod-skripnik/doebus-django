from django.db.models.query import RawQuerySet

from app.services import BaseService
from examples.models import Pet


class InnerJoiner(BaseService):
    """
    Inner join selects rows,
    which are matching in both left table (FROM)
    and right table (JOIN)
    """

    QUERY = """
        SELECT
            examples_pet.id,
            examples_person.id,
            examples_person.name AS owner_name
        FROM examples_pet
        INNER JOIN examples_person ON examples_pet.owner_id = examples_person.id;
    """

    def act(self) -> RawQuerySet:
        return Pet.objects.raw(self.QUERY)
