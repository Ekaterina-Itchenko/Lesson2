from dataclasses import dataclass


@dataclass
class BasketsBooksDTO:
    basket_id: int
    book_id: int
    quantity: int
