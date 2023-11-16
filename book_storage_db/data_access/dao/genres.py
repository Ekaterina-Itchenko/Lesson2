from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import GenresDTO


class GenresDAO(BaseDAO):
    def create(self, data: GenresDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO genres(genre_name, genre_description) '
            'VALUES(?, ?);', (
                data.genre_name,
                data.description
            )
        )
        self._db_connector.connection.commit()

    def get_id_list(self) -> list[int]:
        res = self._db_connector.cursor.execute(
            'SELECT genre_id FROM genres;'
        )
        return res.fetchall()
