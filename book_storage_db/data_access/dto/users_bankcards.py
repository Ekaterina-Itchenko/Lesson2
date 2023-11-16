from dataclasses import dataclass


@dataclass
class UsersBankcardsDTO:
    user_id: int
    bankcard_id: int
