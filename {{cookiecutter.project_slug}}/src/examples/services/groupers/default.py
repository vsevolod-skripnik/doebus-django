from typing import List

from django.db import connection

from app.services import BaseService


class DefaultGrouper(BaseService):
    """
    Grouping by is an operation,
    which selects values against GROUP BY fields
    """

    QUERY = """
        SELECT
            COUNT(examples_pet.id),
            examples_pet.owner_id
        FROM examples_pet
        GROUP BY examples_pet.owner_id;
    """

    def act(self) -> List[tuple]:
        with connection.cursor() as cursor:
            cursor.execute(self.QUERY)
            return cursor.fetchall()
