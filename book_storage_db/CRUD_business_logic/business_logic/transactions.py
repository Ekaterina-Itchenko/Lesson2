from __future__ import annotations
from data_access.dao import TransactionsDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...data_access.interfaces import ConnectorProto
    from ...data_access.dto import TransactionInfoDTO


class TransactionsService:
    def __init__(self, db_connector: ConnectorProto) -> None:
        self._dao = TransactionsDAO(db_connector)

    def get_info(self) -> list[TransactionInfoDTO]:
        return self._dao.get_all_transactions_info()
