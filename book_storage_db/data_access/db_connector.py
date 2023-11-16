from __future__ import annotations
import sqlite3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sqlite3 import Connection, Cursor


class SqliteConnector:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.connection = self._create_connector()
        self.cursor = self._create_cursor()

    def _create_connector(self) -> Connection:
        return sqlite3.connect(self.db_name)

    def _create_cursor(self) -> Cursor:
        return self.connection.cursor()
