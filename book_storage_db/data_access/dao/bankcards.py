from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import BankcardsDTO


class BankcardsDAO(BaseDAO):
    def create(self, data: BankcardsDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO bankcards(number, first_name, last_name, cvc,'
            ' expiry_date) VALUES(?, ?, ?, ?, ?);', (
                data.number,
                data.first_name,
                data.last_name,
                data.cvc,
                data.expiry_date)
        )
        self._db_connector.connection.commit()

    def get_id_list(self) -> list[int]:
        res = self._db_connector.cursor.execute(
            'SELECT bankcard_id FROM bankcards;'
        )
        return res.fetchall()

    def get_available_id_list_for_transact(self) -> list[tuple[int, int]]:
        res = self._db_connector.cursor.execute(
            'SELECT b.basket_id , ub.bankcard_id FROM baskets b '
            'LEFT JOIN users_bankcards ub ON ub.user_id = b.user_id '
            'ORDER BY b.basket_id;'
        ).fetchall()
        return res
