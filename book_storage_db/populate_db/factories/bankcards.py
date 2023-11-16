from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import BankcardsDTO
if TYPE_CHECKING:
    from ..fake_lib import (BankCardProvider,
                            NameProvider,
                            LastNameProvider,
                            CvcProvider,
                            ExpiryDateProvider)


class BankcardsFactory:
    def __init__(
            self,
            number: BankCardProvider,
            first_name: NameProvider,
            last_name: LastNameProvider,
            cvc: CvcProvider,
            expiry_date: ExpiryDateProvider
      ) -> None:
        self._number = number
        self._first_name = first_name
        self._last_name = last_name
        self._cvc = cvc
        self._expiry_date = expiry_date

    def generate(self) -> BankcardsDTO:
        return BankcardsDTO(number=self._number(),
                            first_name=self._first_name(),
                            last_name=self._last_name(),
                            cvc=self._cvc(),
                            expiry_date=self._expiry_date())
