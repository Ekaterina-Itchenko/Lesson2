from dataclasses import dataclass
from typing import Optional


@dataclass
class AuthorsDTO:
    first_name: str
    last_name: str
    birth_date: object
    death_date: Optional[object]
    information: str
