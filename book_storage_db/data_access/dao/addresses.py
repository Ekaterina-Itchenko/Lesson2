from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import AddressesDTO


class AddressesDAO(BaseDAO):
    def create(self, data: AddressesDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO addresses(country, city, street,'
            ' home_number, post_code) VALUES(?, ?, ?, ?, ?);',
            (
                data.country,
                data.city,
                data.street,
                data.home_number,
                data.post_code
            )
        )
        self._db_connector.connection.commit()

    def get_id_list(self) -> list[int]:
        res = self._db_connector.cursor.execute(
            'SELECT address_id FROM addresses;'
        )
        return res.fetchall()
