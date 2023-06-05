from interfaces import ConnectorProtocol
from api_connector import OpenweathermapConnector


def provide_api(api_name: str, city: str) -> ConnectorProtocol:
    if api_name == "openweathermap.org":
        return OpenweathermapConnector(city)
    else:
        raise ValueError("Unsupported API.")
