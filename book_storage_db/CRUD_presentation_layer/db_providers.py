from __future__ import annotations
from data_access import SqliteConnector
from data_access.interfaces import ConnectorProto


def db_provider(db_name: str, db_type: str) -> ConnectorProto:
    if db_type == 'sqlite':
        return SqliteConnector(db_name=db_name)
