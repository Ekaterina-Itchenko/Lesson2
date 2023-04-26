from dataclasses import dataclass


@dataclass
class AddressesDTO:
    country: str
    city: str
    street: str
    home_number: int
    post_code: int
