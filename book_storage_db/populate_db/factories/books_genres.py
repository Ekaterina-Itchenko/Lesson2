from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import BooksGenresDTO
if TYPE_CHECKING:
    from ..fake_lib import RandomIdProvider


class BooksGenresFactory:
    def __init__(
            self,
            book_id: RandomIdProvider,
            genre_id: RandomIdProvider
      ) -> None:
        self._genre_id = genre_id
        self._book_id = book_id

    def generate(self) -> BooksGenresDTO:
        return BooksGenresDTO(genre_id=self._genre_id(),
                              book_id=self._book_id())
