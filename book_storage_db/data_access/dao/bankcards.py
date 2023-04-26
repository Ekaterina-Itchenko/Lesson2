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
