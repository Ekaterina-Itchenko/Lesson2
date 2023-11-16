from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import BooksAuthorsDTO


class BooksAuthorsDAO(BaseDAO):
    def create(self, data: BooksAuthorsDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO books_authors (book_id, author_id) VALUES (?, ?);',
            (
                data.book_id,
                data.author_id
            )
        )
        self._db_connector.connection.commit()
