from dataclasses import dataclass


@dataclass
class CompanyDTO:
    symbol: str
    name: str
    sector: str
    price: float
