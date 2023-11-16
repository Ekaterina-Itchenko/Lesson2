from dataclasses import dataclass


@dataclass
class BooksDTO:
    title: str
    price: float
    description: str
    pages: int
    book_format: str
    age_limit: int
    amount: int
