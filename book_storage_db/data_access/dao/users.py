from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import UsersDTO


class UsersDAO(BaseDAO):
    def create(self, data: UsersDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO users(first_name, last_name, user_name, age, email,'
            ' phone_number, password) VALUES(?, ?, ?, ?, ?, ?, ?);', (
                data.first_name,
                data.last_name,
                data.user_name,
                data.age,
                data.email,
                data.phone_number,
                data.password
            )
        )
        self._db_connector.connection.commit()

    def get_id_list(self) -> list[int]:
        res = self._db_connector.cursor.execute(
            'SELECT user_id FROM users;'
        )
        return res.fetchall()
