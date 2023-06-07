from dataclasses import dataclass
from typing import Optional


@dataclass
class Coord:
    lon: Optional[float]
    lat: Optional[float]


@dataclass
class WeatherInfo:
    id: int    # noqa A003
    main: str
    description: str
    icon: str


@dataclass
class MainInfo:
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: Optional[int]
    grnd_level: Optional[int]


@dataclass
class WindInfo:
    speed: float
    deg: int
    gust: Optional[float]


@dataclass
class CloudInfo:
    all: int  # noqa A003


@dataclass
class SysInfo:
    type: Optional[int]      # noqa A003
    id: Optional[int]        # noqa A003
    country: str
    sunrise: int
    sunset: int


@dataclass
class WeatherConditionsDTO:
    coord: Coord
    weather: list[WeatherInfo]
    base: str
    main: MainInfo
    visibility: int
    wind: WindInfo
    clouds: CloudInfo
    dt: int
    sys: SysInfo
    timezone: int
    id: int          # noqa A003
    name: str
    cod: int
    message: Optional[str]
