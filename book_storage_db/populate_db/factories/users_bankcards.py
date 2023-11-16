from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import UsersBankcardsDTO
if TYPE_CHECKING:
    from ..fake_lib import RandomIdProvider


class UsersBankcardsFactory:
    def __init__(
            self,
            user_id: RandomIdProvider,
            bankcard_id: RandomIdProvider
      ) -> None:
        self._user_id = user_id
        self._bankcard_id = bankcard_id

    def generate(self) -> UsersBankcardsDTO:
        return UsersBankcardsDTO(user_id=self._user_id(),
                                 bankcard_id=self._bankcard_id())
