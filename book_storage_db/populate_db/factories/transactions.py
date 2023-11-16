from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import TransactionsDTO
if TYPE_CHECKING:
    from ..fake_lib import (RandomIdProvider,
                            FloatDigitProvider,
                            AvailableIdProvider)


class TransactionsFactory:
    def __init__(
            self,
            basket_id: RandomIdProvider,
            bankcard_id: AvailableIdProvider,
            amount: FloatDigitProvider,
            address_id: AvailableIdProvider,

      ) -> None:
        self._basket_id = basket_id
        self._bankcard_id = bankcard_id
        self._amount = amount
        self._address_id = address_id

    def generate(self) -> TransactionsDTO:
        bk_id = self._basket_id()
        return TransactionsDTO(basket_id=bk_id,
                               bankcard_id=self._bankcard_id(basket_id=bk_id),
                               amount=self._amount(),
                               address_id=self._address_id(basket_id=bk_id))
