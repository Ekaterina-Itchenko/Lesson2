from __future__ import annotations
from data_access.dao import BooksDAO
from .errors import InvalidIdError
from typing import TYPE_CHECKING, Any
if TYPE_CHECKING:
    from ...data_access.interfaces import ConnectorProto


class BooksService:
    def __init__(self, db_connector: ConnectorProto) -> None:
        self._dao = BooksDAO(db_connector)

    def get_all_books_list(self) -> list[tuple[Any]]:
        return self._dao.get_list_of_all_books()

    def get_book_info(self, book_id: int) -> str:
        id_list = [item[0] for item in self._dao.get_id_list()]
        if book_id not in id_list:
            raise InvalidIdError("The id is not exist.")
        book_info = self._dao.get_book_info(book_id=book_id)
        return f'Id: {book_info.book_id}\n' \
               f'Name: {book_info.title}\n' \
               f'Age: {book_info.age_limit}\n' \
               f'Price: {book_info.price}\n' \
               f'Description: {book_info.description}\n' \
               f'Authors: {book_info.authors}\n' \
               f'Pages: {book_info.pages}\n' \
               f'Genres: {book_info.genres}\n' \
               f'Quantity: {book_info.quantity}\n' \
               f'Added to shop: {book_info.add_to_shop}'

    def delete_book(self, book_id: int) -> None:
        id_list = [item[0] for item in self._dao.get_id_list()]
        if book_id not in id_list:
            raise InvalidIdError("The id is not exist.")
        self._dao.delete_book(book_id=book_id)

    def update_book_name(self, book_id: int, new_name: str) -> None:
        id_list = [item[0] for item in self._dao.get_id_list()]
        if book_id not in id_list:
            raise InvalidIdError("The id is not exist.")
        self._dao.update_book_name(book_id=book_id, new_name=new_name)
