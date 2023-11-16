from dataclasses import dataclass


@dataclass
class BankcardsDTO:
    number: int
    first_name: str
    last_name: str
    cvc: int
    expiry_date: str
