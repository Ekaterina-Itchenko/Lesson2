from __future__ import annotations
from requests import Session
from DTO import WeatherConditionsDTO
from dacite import from_dict, MissingValueError
from config import API_URL, API_KEY


class OpenweathermapAdapter:
    def __init__(self, session: Session) -> None:
        self._session = session

    def get_weather(self, city: str) -> WeatherConditionsDTO:
        try:
            response = self._session.get(
                url=API_URL + "data/2.5/weather",
                params={'q': city.strip(),
                        'appid': API_KEY,
                        'units': 'metric'}
            )
            result = from_dict(WeatherConditionsDTO, data=response.json())
            return result
        except MissingValueError:
            raise ValueError(f'The city "{city}" has not found.')
