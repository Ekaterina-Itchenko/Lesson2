from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import UsersRolesDTO
if TYPE_CHECKING:
    from ..fake_lib import RandomIdProvider


class UsersRolesFactory:
    def __init__(
            self,
            user_id: RandomIdProvider,
            role_id: RandomIdProvider
      ) -> None:
        self._user_id = user_id
        self._role_id = role_id

    def generate(self) -> UsersRolesDTO:
        return UsersRolesDTO(user_id=self._user_id(),
                             role_id=self._role_id())
