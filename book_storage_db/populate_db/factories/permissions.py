from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import PermissionsDTO
if TYPE_CHECKING:
    from ..fake_lib import PermissionProvider


class PermissionsFactory:
    def __init__(
            self,
            permission_name: PermissionProvider
    ) -> None:
        self._permission_name = permission_name

    def generate(self) -> PermissionsDTO:
        return PermissionsDTO(name=self._permission_name())
