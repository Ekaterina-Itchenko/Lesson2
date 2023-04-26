from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import TransactionsDTO
if TYPE_CHECKING:
    from ..fake_lib import (RandomIdProvider, FloatDigitProvider)


class TransactionsFactory:
    def __init__(
            self,
            basket_id: RandomIdProvider,
            bankcard_id: RandomIdProvider,
            amount: FloatDigitProvider,
            address_id: RandomIdProvider,

      ) -> None:
        self._basket_id = basket_id
        self._bankcard_id = bankcard_id
        self._amount = amount
        self._address_id = address_id

    def generate(self) -> TransactionsDTO:
        return TransactionsDTO(basket_id=self._basket_id(),
                               bankcard_id=self._bankcard_id(),
                               amount=self._amount(),
                               address_id=self._address_id())
