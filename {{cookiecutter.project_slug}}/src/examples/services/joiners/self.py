from django.db.models.query import RawQuerySet

from app.services import BaseService
from examples.models import Pet


class SelfJoiner(BaseService):
    """
    Self join selects rows from current table,
    which match specified condition
    """

    QUERY = """
        SELECT
            pet.id,
            pet.name AS self_name,
            another.name AS another_name
        FROM examples_pet pet, examples_pet another
        WHERE
            pet.owner_id = another.owner_id
            AND pet.id <> another.id
        ;
    """

    def act(self) -> RawQuerySet:
        return Pet.objects.raw(self.QUERY)
