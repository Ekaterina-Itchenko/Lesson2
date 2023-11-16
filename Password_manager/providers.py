from data import (KeyStorage,
                  PasswordStorage,
                  CsvExporter,
                  JsonExporter,
                  ExcelExporter,
                  TxtExporter,
                  XmlExporter)
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from interfaces import ExporterProto


def key_provider(key_storage: str,
                 code_phrase_storage: str) -> 'KeyStorage':
    if (key_storage.split('.')[1] == 'json' and
            code_phrase_storage.split('.')[1] == 'json'):
        return KeyStorage(key_storage, code_phrase_storage)
    else:
        raise ValueError("Unsupported DB type.")


def password_provider(file_name: str) -> 'PasswordStorage':
    if file_name.split('.')[1] == 'json':
        return PasswordStorage(file_name)
    else:
        raise ValueError("Unsupported DB type.")


def export_provider(file_name: str) -> 'ExporterProto':
    if file_name.split('.')[1] == 'json':
        return JsonExporter(file_name)
    elif file_name.split('.')[1] == 'csv':
        return CsvExporter(file_name)
    elif file_name.split('.')[1] == 'xlsx' or file_name.split('.')[1] == 'xls':
        return ExcelExporter(file_name)
    elif file_name.split('.')[1] == 'txt':
        return TxtExporter(file_name)
    elif file_name.split('.')[1] == 'xml':
        return XmlExporter(file_name)
    else:
        raise ValueError("Unsupported DB type.")
