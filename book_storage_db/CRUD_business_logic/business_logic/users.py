from data_access.dao import UsersDAO
from data_access.interfaces import ConnectorProto
from .errors import InvalidIdError
from typing import Any


class UserService:
    def __init__(self, db_connector: ConnectorProto) -> None:
        self._dao = UsersDAO(db_connector)

    def get_all_users_list(self) -> list[tuple[Any]]:
        return self._dao.get_list_of_all_users()

    def get_user_info(self, user_id: int) -> str:
        id_list = [item[0] for item in self._dao.get_id_list()]
        if user_id not in id_list:
            raise InvalidIdError('The id is not exist.')
        res = self._dao.get_user_info(user_id=user_id)
        return f'Id: {res.user_id}\n' \
               f'Name: {res.name}\n' \
               f'Surname: {res.surname}\n' \
               f'Email: {res.email}\n' \
               f'Phone: {res.phone_number}\n' \
               f'Age: {res.age}\n' \
               f'Registration_date: {res.registration_date}\n' \
               f'Roles: {res.roles}'

    def delete_user(self, user_id: int) -> None:
        id_list = [item[0] for item in self._dao.get_id_list()]
        if user_id not in id_list:
            raise InvalidIdError('The id is not exist.')
        self._dao.delete_user(user_id=user_id)

    def update_user_email(self, user_id: int, new_email: str) -> None:
        id_list = [item[0] for item in self._dao.get_id_list()]
        if user_id not in id_list:
            raise InvalidIdError('The id is not exist.')
        self._dao.update_user_email(user_id=user_id, email=new_email)

    def update_user_phone(self, user_id: int, new_phone: str) -> None:
        id_list = [item[0] for item in self._dao.get_id_list()]
        if user_id not in id_list:
            raise InvalidIdError('The id is not exist.')
        self._dao.update_user_phone(user_id=user_id, phone=new_phone)
