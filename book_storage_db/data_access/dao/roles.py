from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import RolesDTO


class RolesDAO(BaseDAO):
    def create(self, data: RolesDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO roles(role_name) VALUES(?);',
            (data.name, ))
        self._db_connector.connection.commit()

    def get_id_list(self) -> list[int]:
        res = self._db_connector.cursor.execute('SELECT role_id FROM roles;')
        return res.fetchall()
