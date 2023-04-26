from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import AuthorsDTO


class AuthorsDAO(BaseDAO):
    def create(self, data: AuthorsDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO authors(first_name, last_name, birth_date,'
            ' date_of_death, information) VALUES(?, ?, ?, ?, ?);',
            (
                data.first_name,
                data.last_name,
                data.birth_date,
                data.death_date,
                data.information)
        )
        self._db_connector.connection.commit()

    def get_id_list(self) -> list[int]:
        res = self._db_connector.cursor.execute(
            'SELECT author_id FROM authors;'
        )
        return res.fetchall()
