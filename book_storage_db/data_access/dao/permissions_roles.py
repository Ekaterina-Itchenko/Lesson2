from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import PermissionsRolesDTO


class PermissionsRolesDAO(BaseDAO):
    def create(self, data: PermissionsRolesDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO permissions_roles (permission_id, role_id)'
            ' VALUES (?, ?);', (
                data.permission_id,
                data.role_id
            )
        )
        self._db_connector.connection.commit()
