from __future__ import annotations
from interfaces import AdapterProtocol
from api_adapters import OpenweathermapAdapter
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from requests import Session


def provide_api(api_url: str, session: Session) -> AdapterProtocol:
    if api_url == 'https://api.openweathermap.org/':
        return OpenweathermapAdapter(session=session)
    else:
        raise ValueError("Unsupported API.")
