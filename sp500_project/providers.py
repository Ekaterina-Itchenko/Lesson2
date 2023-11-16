from data_access import Sp500Csv, Sp500Json
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from interfaces import DbProto


def provider(file_extension: str, db_name: str) -> 'DbProto':
    if file_extension == '.csv':
        return Sp500Csv(db_name)
    elif file_extension == '.json':
        return Sp500Json(db_name)
    else:
        raise ValueError("Unsupported DB type.")
