from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import TransactionsDTO


class TransactionsDAO(BaseDAO):
    def create(self, data: TransactionsDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO transactions(basket_id, bankcard_id, amount,'
            ' address_id) VALUES(?, ?, ?, ?);', (
                data.basket_id,
                data.bankcard_id,
                data.amount,
                data.address_id
            )
        )
        self._db_connector.connection.commit()
