from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import BasketsBooksDTO
if TYPE_CHECKING:
    from ..fake_lib import RandomIdProvider, DigitProvider


class BasketsBooksFactory:
    def __init__(
            self,
            basket_id: RandomIdProvider,
            book_id: RandomIdProvider,
            quantity: DigitProvider
      ) -> None:
        self._basket_id = basket_id
        self._book_id = book_id
        self._quantity = quantity

    def generate(self) -> BasketsBooksDTO:
        return BasketsBooksDTO(basket_id=self._basket_id(),
                               book_id=self._book_id(),
                               quantity=self._quantity())
