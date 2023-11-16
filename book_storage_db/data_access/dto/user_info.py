from dataclasses import dataclass


@dataclass
class UsersInfoDTO:
    user_id: int
    name: str
    surname: str
    email: str
    phone_number: str
    age: int
    registration_date: object
    roles: list[str]
