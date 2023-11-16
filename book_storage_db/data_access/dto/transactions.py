from dataclasses import dataclass


@dataclass
class TransactionsDTO:
    basket_id: int
    bankcard_id: int
    amount: float
    address_id: int
