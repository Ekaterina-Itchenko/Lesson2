from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import UsersRolesDTO


class UsersRolesDAO(BaseDAO):
    def create(self, data: UsersRolesDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO users_roles (user_id, role_id) VALUES (?, ?);',
            (data.user_id, data.role_id))
        self._db_connector.connection.commit()
