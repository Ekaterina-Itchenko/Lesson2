from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import BooksAuthorsDTO
if TYPE_CHECKING:
    from ..fake_lib import RandomIdProvider


class BooksAuthorsFactory:
    def __init__(
            self,
            book_id: RandomIdProvider,
            author_id: RandomIdProvider
      ) -> None:
        self._author_id = author_id
        self._book_id = book_id

    def generate(self) -> BooksAuthorsDTO:
        return BooksAuthorsDTO(author_id=self._author_id(),
                               book_id=self._book_id())
