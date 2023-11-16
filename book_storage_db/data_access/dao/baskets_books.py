from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import BasketsBooksDTO


class BasketsBooksDAO(BaseDAO):
    def create(self, data: BasketsBooksDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO baskets_books (basket_id, book_id, quantity) '
            'VALUES (?, ?, ?);',
            (
                data.basket_id,
                data.book_id,
                data.quantity
            )
        )
        self._db_connector.connection.commit()
