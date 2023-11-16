from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import RolesDTO
if TYPE_CHECKING:
    from ..fake_lib import RoleProvider


class RolesFactory:
    def __init__(
            self,
            role_name: RoleProvider
    ) -> None:
        self._role_name = role_name

    def generate(self) -> RolesDTO:
        return RolesDTO(name=self._role_name())
