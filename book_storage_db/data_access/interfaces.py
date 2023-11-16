from __future__ import annotations
from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from sqlite3 import Connection, Cursor


class ConnectorProto(Protocol):
    connection: Connection
    cursor: Cursor


class CreateRecordProto(Protocol):
    def create(self, data: object) -> None:
        raise NotImplementedError
