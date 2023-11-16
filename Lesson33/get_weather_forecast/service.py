from __future__ import annotations
from DTO import WeatherConditionsDTO
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from interfaces import AdapterProtocol


class WeatherService:
    def __init__(self, api_adapter: AdapterProtocol) -> None:
        self._weather_api = api_adapter

    def get_weather_in_cities(self, cities: str) -> list[WeatherConditionsDTO]:
        cities = cities.split(',')
        result: list[WeatherConditionsDTO] = []
        for city in cities:
            weather_data = self._weather_api.get_weather(city=city)
            result.append(weather_data)

        return result
