from dataclasses import dataclass


@dataclass
class WeatherConditionsDTO:
    city: str
    temperature: float
    desc: str
    humidity: float
