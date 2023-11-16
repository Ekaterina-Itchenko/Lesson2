from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import PermissionsRolesDTO
if TYPE_CHECKING:
    from ..fake_lib import RandomIdProvider


class PermissionsRolesFactory:
    def __init__(
            self,
            permission_id: RandomIdProvider,
            role_id: RandomIdProvider
      ) -> None:
        self._permission_id = permission_id
        self._role_id = role_id

    def generate(self) -> PermissionsRolesDTO:
        return PermissionsRolesDTO(permission_id=self._permission_id(),
                                   role_id=self._role_id())
