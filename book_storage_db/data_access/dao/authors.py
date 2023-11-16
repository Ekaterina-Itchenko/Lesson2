from __future__ import annotations
from .base_dao import BaseDAO
from ..dto import AuthorsDTO, AuthorInfoDTO
from typing import Any


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

    def get_list_of_all(self) -> list[tuple[Any]]:
        res = self._db_connector.cursor.execute(
            'SELECT author_id, first_name, last_name FROM authors '
            'ORDER BY first_name, last_name;'
        )
        return res.fetchall()

    def get_author_info(self, author_id: int) -> AuthorInfoDTO:
        author_info = self._db_connector.cursor.execute(
            'SELECT author_id, first_name, last_name, birth_date, '
            'date_of_death, information FROM authors WHERE '
            'author_id = (?);', (author_id, )
        ).fetchall()
        return AuthorInfoDTO(author_id=author_info[0][0],
                             first_name=author_info[0][1],
                             last_name=author_info[0][2],
                             birth_date=author_info[0][3],
                             death_date=author_info[0][4],
                             information=author_info[0][5])
