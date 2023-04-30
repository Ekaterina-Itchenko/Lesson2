from __future__ import annotations
from .base_dao import BaseDAO
from ..dto import UsersInfoDTO
from typing import TYPE_CHECKING, Any
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

    def get_id_list(self) -> list[tuple[int]]:
        res = self._db_connector.cursor.execute(
            'SELECT user_id FROM users;'
        )
        return res.fetchall()

    def get_list_of_all_users(self) -> list[tuple[Any]]:
        res = self._db_connector.cursor.execute(
            'SELECT user_id, first_name, last_name, email,'
            ' created_at FROM users ORDER BY first_name, last_name;'
        )
        return res.fetchall()

    def get_user_info(self, user_id: int) -> UsersInfoDTO:
        res = self._db_connector.cursor.execute(
            'SELECT users.user_id, users.first_name, users.last_name, '
            'users.email, users.phone_number, users.age, users.created_at, '
            'r.role_name '
            'FROM users '
            'LEFT JOIN users_roles ur ON users.user_id = ur.user_id '
            'LEFT JOIN roles r ON ur.role_id = r.role_id '
            'WHERE users.user_id = (?);', (user_id, )
        ).fetchall()
        return UsersInfoDTO(user_id=res[0][0],
                            name=res[0][1],
                            surname=res[0][2],
                            email=res[0][3],
                            phone_number=res[0][4],
                            age=res[0][5],
                            registration_date=res[0][6],
                            roles=[item[-1] for item in res])

    def delete_user(self, user_id: int) -> None:
        self._db_connector.cursor.execute(
            'DELETE FROM users WHERE user_id = (?);', (user_id, )
        )
        self._db_connector.connection.commit()

    def update_user_phone(self, user_id: int, phone: str) -> None:
        self._db_connector.cursor.execute(
            'UPDATE users SET phone_number = (?), '
            'updated_at = CURRENT_TIMESTAMP WHERE user_id = (?);',
            (phone, user_id)
        )
        self._db_connector.connection.commit()

    def update_user_email(self, user_id: int, email: str) -> None:
        self._db_connector.cursor.execute(
            'UPDATE users SET email = (?), updated_at = CURRENT_TIMESTAMP'
            ' WHERE user_id = (?);', (email, user_id)
        )
        self._db_connector.connection.commit()
