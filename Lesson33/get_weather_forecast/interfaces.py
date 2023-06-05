from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from DTO import WeatherConditionsDTO


class ConnectorProtocol(Protocol):
    city: str
    key: str
    url: str
    params: dict

    def get_weather(self) -> 'WeatherConditionsDTO':
        pass
