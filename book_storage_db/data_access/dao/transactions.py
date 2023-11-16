from __future__ import annotations
from .base_dao import BaseDAO
from data_access.dto import TransactionInfoDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..dto import TransactionsDTO


class TransactionsDAO(BaseDAO):
    def create(self, data: TransactionsDTO) -> None:
        self._db_connector.cursor.execute(
            'INSERT INTO transactions(basket_id, bankcard_id, amount,'
            ' address_id) VALUES(?, ?, ?, ?);', (
                data.basket_id,
                data.bankcard_id,
                data.amount,
                data.address_id
            )
        )
        self._db_connector.connection.commit()

    def get_all_transactions_info(self) -> list[TransactionInfoDTO]:
        transaction_info = self._db_connector.cursor.execute(
            'SELECT u.first_name, u.last_name, b2.number, t.amount, '
            't.updated_at, a.city , a.street , a.home_number , a.post_code '
            'FROM transactions t '
            'LEFT JOIN baskets b ON t.basket_id = b.basket_id '
            'LEFT JOIN users u ON b.user_id = u.user_id '
            'LEFT JOIN bankcards b2 ON t.bankcard_id = b2.bankcard_id '
            'LEFT JOIN addresses a ON t.address_id = a.address_id;'
        ).fetchall()
        res = []
        for item in transaction_info:
            res.append(TransactionInfoDTO(
                name=item[0],
                surname=item[1],
                bankcard_number=item[2],
                amount=item[3],
                updated_at=item[4],
                address=f'city:{item[5]} street:{item[6]}, '
                        f'home number:{item[7]} post code:{item[8]}'
            ))
        return res
