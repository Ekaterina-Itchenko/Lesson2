from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import UsersAddressesDTO
if TYPE_CHECKING:
    from ..fake_lib import RandomIdProvider


class UsersAddressesFactory:
    def __init__(
            self,
            user_id: RandomIdProvider,
            address_id: RandomIdProvider
      ) -> None:
        self._user_id = user_id
        self._address_id = address_id

    def generate(self) -> UsersAddressesDTO:
        return UsersAddressesDTO(user_id=self._user_id(),
                                 address_id=self._address_id())
