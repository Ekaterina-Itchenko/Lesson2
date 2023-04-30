from dataclasses import dataclass


@dataclass
class TransactionInfoDTO:
    name: str
    surname: str
    bankcard_number: int
    amount: float
    updated_at: object
    address: str
