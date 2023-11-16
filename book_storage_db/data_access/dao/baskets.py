from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import BasketsDTO


class BasketsDAO(BaseDAO):
    def create(self, data: BasketsDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO baskets(user_id, status) VALUES(?, ?);',
            (
                data.user_id,
                data.status
            )
        )
        self._db_connector.connection.commit()

    def get_id_list(self) -> list[int]:
        res = self._db_connector.cursor.execute(
            'SELECT basket_id FROM baskets;'
        )
        return res.fetchall()
