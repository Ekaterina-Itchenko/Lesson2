from __future__ import annotations
import requests
from DTO import WeatherConditionsDTO


class OpenweathermapConnector:
    def __init__(self, city: str) -> None:
        self.city = city
        self.key = '4bfa99624e944937c0a6fb04c749f887'
        self.url = 'https://api.openweathermap.org/data/2.5/weather'
        self.params = self._get_params()

    # @property
    def _get_params(self) -> dict:
        params = {'q': self.city, 'appid': self.key, 'units': 'metric'}
        return params

    def get_weather(self) -> WeatherConditionsDTO:
        parameters = self.params
        url = self.url
        data = requests.get(url=url, params=parameters).json()
        return WeatherConditionsDTO(city=self.city.capitalize(),
                                    temperature=data['main']['temp'],
                                    desc=data["weather"][0]["description"],
                                    humidity=data["main"]["humidity"])
