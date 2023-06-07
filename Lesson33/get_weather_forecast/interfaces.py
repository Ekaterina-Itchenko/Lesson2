from __future__ import annotations
from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from DTO import WeatherConditionsDTO


class AdapterProtocol(Protocol):
    def get_weather(self, city: str) -> WeatherConditionsDTO:
        pass
