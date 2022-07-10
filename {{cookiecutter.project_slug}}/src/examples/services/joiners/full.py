from django.db.models.query import RawQuerySet

from app.services import BaseService
from examples.models import Pet


class FullJoiner(BaseService):
    """
    Full join selects rows,
    which are present in left table (FROM)
    and present in right table (JOIN)
    """

    QUERY = """
        SELECT
            examples_pet.id,
            examples_person.id,
            examples_person.name AS owner_name
        FROM examples_pet
        FULL JOIN examples_person ON examples_pet.owner_id = examples_person.id;
    """

    def act(self) -> RawQuerySet:
        return Pet.objects.raw(self.QUERY)
