from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import UsersAddressesDTO


class UsersAddressesDAO(BaseDAO):
    def create(self, data: UsersAddressesDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO users_addresses(user_id, address_id) VALUES(?, ?);',
            (data.user_id, data.address_id))
        self._db_connector.connection.commit()
