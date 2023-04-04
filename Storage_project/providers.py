from data_access import StorageJson, CategoriesJson, OrdersJson
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from interfaces import StorageProto, OrdersProto, CategoriesProto


def provide_st(db_type: str, db_file: str) -> 'StorageProto':
    if db_type == "json":
        return StorageJson(db_file)
    else:
        raise ValueError("Unsupported DB type.")


def provide_ct(db_type: str, db_file: str) -> 'CategoriesProto':
    if db_type == "json":
        return CategoriesJson(db_file)
    else:
        raise ValueError("Unsupported DB type.")


def provide_ord(db_type: str, db_file: str) -> 'OrdersProto':
    if db_type == "json":
        return OrdersJson(db_file)
    else:
        raise ValueError("Unsupported DB type.")
