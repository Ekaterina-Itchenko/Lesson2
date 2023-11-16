from __future__ import annotations
from data_access.dao import AuthorsDAO
from .errors import InvalidIdError
from typing import TYPE_CHECKING, Any
if TYPE_CHECKING:
    from ...data_access.interfaces import ConnectorProto


class AuthorsService:
    def __init__(self, db_connector: ConnectorProto) -> None:
        self._dao = AuthorsDAO(db_connector)

    def get_all_authors_info(self) -> list[tuple[Any]]:
        return self._dao.get_list_of_all()

    def get_author_info(self, author_id: int) -> str:
        id_list = [item[0] for item in self._dao.get_id_list()]
        if author_id not in id_list:
            raise InvalidIdError("The id is not exist.")
        author_info = self._dao.get_author_info(author_id)
        return f'Id: {author_info.author_id}\n' \
               f'Name: {author_info.first_name}\n' \
               f'Surname: {author_info.last_name}\n' \
               f'Date of birth: {author_info.birth_date}\n' \
               f'Date of death: {author_info.death_date}\n' \
               f'Information: {author_info.information}'
