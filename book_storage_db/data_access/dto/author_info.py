from dataclasses import dataclass
from typing import Optional


@dataclass
class AuthorInfoDTO:
    author_id: int
    first_name: str
    last_name: str
    birth_date: object
    death_date: Optional[object]
    information: str
