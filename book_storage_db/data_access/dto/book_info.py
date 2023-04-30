from dataclasses import dataclass


@dataclass
class BookInfoDTO:
    book_id: int
    title: str
    age_limit: int
    price: float
    description: str
    authors: list[str]
    pages: int
    genres: list[str]
    quantity: int
    add_to_shop: object
