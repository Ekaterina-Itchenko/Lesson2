from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..interfaces import ConnectorProto


class BaseDAO:
    def __init__(self, db_connector: ConnectorProto) -> None:
        self._db_connector = db_connector
