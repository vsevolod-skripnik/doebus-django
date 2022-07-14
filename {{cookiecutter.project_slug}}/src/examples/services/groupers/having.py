from typing import List

from django.db import connection

from app.base.services import BaseService


class HavingGrouper(BaseService):
    """
    Having keyword works like WHERE keyword,
    but in GROUP BY statements
    """

    QUERY = """
        SELECT
            COUNT(examples_pet.id),
            examples_pet.owner_id
        FROM examples_pet
        GROUP BY examples_pet.owner_id
        HAVING COUNT(examples_pet.id) > 1;
    """

    def act(self) -> List[tuple]:
        with connection.cursor() as cursor:
            cursor.execute(self.QUERY)
            return cursor.fetchall()
