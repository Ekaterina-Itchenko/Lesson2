from __future__ import annotations
from .base_dao import BaseDAO
from ..dto import BookInfoDTO
from typing import TYPE_CHECKING, Any
if TYPE_CHECKING:
    from ..dto import BooksDTO


class BooksDAO(BaseDAO):
    def create(self, data: BooksDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO books(title, price, description, pages, format,'
            ' age_limit, amount) VALUES(?, ?, ?, ?, ?, ?, ?);',
            (
                data.title,
                data.price,
                data.description,
                data.pages,
                data.book_format,
                data.age_limit,
                data.amount
            )
        )
        self._db_connector.connection.commit()

    def get_id_list(self) -> list[int]:
        res = self._db_connector.cursor.execute(
            'SELECT book_id FROM books;'
        )
        return res.fetchall()

    def get_list_of_all_books(self) -> list[tuple[Any]]:
        res = self._db_connector.cursor.execute(
            'SELECT book_id, title, pages, price,'
            ' age_limit, amount FROM books ORDER BY title;'
        )
        return res.fetchall()

    def get_book_info(self, book_id: int) -> BookInfoDTO:
        book_info = self._db_connector.cursor.execute(
            'SELECT book_id, title, age_limit, price, description, '
            'pages, amount, updated_at FROM books WHERE'
            ' book_id = (?);', (book_id, )
        ).fetchall()

        authors_list = self._db_connector.cursor.execute(
            'SELECT a.first_name, a.last_name FROM books_authors '
            'LEFT JOIN authors a ON books_authors.author_id = a.author_id '
            'WHERE books_authors.book_id = (?);', (book_id, )
        ).fetchall()
        genres_list = self._db_connector.cursor.execute(
            'SELECT g.genre_name FROM books_genres bg '
            'LEFT JOIN genres g ON bg.genre_id = g.genre_id '
            'WHERE bg.book_id = (?);', (book_id, )
        ).fetchall()

        return BookInfoDTO(
            book_id=book_info[0][0],
            title=book_info[0][1],
            age_limit=book_info[0][2],
            price=book_info[0][3],
            description=book_info[0][4],
            authors=[f'{item[0]} {item[1]}' for item in authors_list],
            pages=book_info[0][5],
            genres=[item[0] for item in genres_list],
            quantity=book_info[0][6],
            add_to_shop=book_info[0][7]
        )

    def delete_book(self, book_id: int) -> None:
        self._db_connector.cursor.execute(
            'DELETE FROM books WHERE book_id = (?);', (book_id, )
        )
        self._db_connector.connection.commit()

    def update_book_name(self, book_id: int, new_name: str) -> None:
        self._db_connector.cursor.execute(
            'UPDATE books SET title = (?), updated_at = CURRENT_TIMESTAMP '
            'WHERE book_id = (?);', (new_name, book_id)
        )
        self._db_connector.connection.commit()
