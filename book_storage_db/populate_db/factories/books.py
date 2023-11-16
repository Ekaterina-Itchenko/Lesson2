from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import BooksDTO
if TYPE_CHECKING:
    from ..fake_lib import (TextProvider,
                            FloatDigitProvider,
                            DigitProvider,
                            BookFormatProvider,
                            TitleBookProvider)


class BooksFactory:
    def __init__(
            self,
            title: TitleBookProvider,
            price: FloatDigitProvider,
            description: TextProvider,
            pages: DigitProvider,
            book_format: BookFormatProvider,
            age_limit: DigitProvider,
            amount: DigitProvider
      ) -> None:
        self._title = title
        self._price = price
        self._description = description
        self._pages = pages
        self._book_format = book_format
        self._age_limit = age_limit
        self._amount = amount

    def generate(self) -> BooksDTO:
        return BooksDTO(title=self._title(),
                        price=self._price(),
                        description=self._description(),
                        pages=self._pages(),
                        book_format=self._book_format(),
                        age_limit=self._age_limit(),
                        amount=self._amount())
