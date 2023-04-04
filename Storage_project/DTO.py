from dataclasses import dataclass


@dataclass
class CategoryStatisticDTO:
    category: list[object]
    quantity: list[int]
    total_revenues: list[float]


@dataclass
class CommonInfoDTO:
    total_revenues: float
    total_amount: int
    popular_category: str
    popular_product: str


@dataclass
class StorageDTO:
    category: str
    created_at: str
    product_id: int
    name: str
    price: str
    quantity: int
    updated_at: str
    add_param: dict[str, str]


@dataclass
class CategoryDTO:
    category: str
    parameters: list[str]


@dataclass
class OrderDTO:
    order_id: int
    goods: list[dict[str, int]]
    order_price: float
    created_at: str
