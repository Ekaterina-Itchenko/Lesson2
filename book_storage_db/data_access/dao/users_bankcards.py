from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import UsersBankcardsDTO


class UsersBankcardsDAO(BaseDAO):
    def create(self, data: UsersBankcardsDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO users_bankcards(user_id, bankcard_id) VALUES(?, ?);',
            (data.user_id, data.bankcard_id))
        self._db_connector.connection.commit()
