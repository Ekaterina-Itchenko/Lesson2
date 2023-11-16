from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import BasketsDTO
if TYPE_CHECKING:
    from ..fake_lib import (RandomIdProvider, BasketStatusProvider)


class BasketsFactory:
    def __init__(
            self,
            user_id: RandomIdProvider,
            status: BasketStatusProvider
      ) -> None:
        self._user_id = user_id
        self._status = status

    def generate(self) -> BasketsDTO:
        return BasketsDTO(user_id=self._user_id(),
                          status=self._status())
