from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import PermissionsDTO


class PermissionsDAO(BaseDAO):
    def create(self, data: PermissionsDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO permissions(permission_name) VALUES(?);',
            (
                data.name,
            )
        )
        self._db_connector.connection.commit()

    def get_id_list(self) -> list[int]:
        res = self._db_connector.cursor.execute(
            'SELECT permission_id FROM permissions;'
        )
        return res.fetchall()
