from dataclasses import dataclass


@dataclass
class UsersDTO:
    first_name: str
    last_name: str
    user_name: str
    age: int
    email: str
    phone_number: str
    password: str
