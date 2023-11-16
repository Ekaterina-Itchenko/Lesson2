from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import BooksDTO


class BooksDAO(BaseDAO):
    def create(self, data: BooksDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO books(title, price, description, pages, format,'
            ' age_limit, amount) VALUES(?, ?, ?, ?, ?, ?, ?);',
            (
                data.title,
                data.price,
                data.description,
                data.pages,
                data.book_format,
                data.age_limit,
                data.amount
            )
        )
        self._db_connector.connection.commit()

    def get_id_list(self) -> list[int]:
        res = self._db_connector.cursor.execute(
            'SELECT book_id FROM books;'
        )
        return res.fetchall()
