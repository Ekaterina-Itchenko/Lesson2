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

    def get_available_id_list_for_transact(self) -> list[tuple[int, int]]:
        res = self._db_connector.cursor.execute(
            'SELECT b.basket_id, ua.address_id  FROM baskets b '
            'LEFT JOIN users_addresses ua ON ua.user_id  = b.user_id '
            'ORDER  BY b.basket_id; '
        ).fetchall()
        return res
