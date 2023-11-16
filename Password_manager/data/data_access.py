import json
from random import choice
import csv
import openpyxl
import xml.etree.ElementTree as Et
from xml.dom import minidom


class KeyStorage:
    def __init__(self, code_storage: str,
                 key_storage: str) -> None:
        self.code_storage = code_storage
        self.key_storage = key_storage

    def generate_key(self) -> str:
        with open(self.code_storage, encoding='utf8') as st_file:
            key: str = choice(json.load(st_file))
            with open(self.key_storage, 'w', encoding='utf8') as k_file:
                json.dump({'code_phrase': key}, k_file)
            return key

    def validate_key_existence(self) -> bool:
        with open(self.key_storage, encoding='utf8') as file:
            key = json.load(file)['code_phrase']
        if key:
            return True
        else:
            return False

    def _get_key(self) -> str:
        with open(self.key_storage, encoding='utf8') as file:
            result: str = json.load(file)['code_phrase']
            return result

    def validate_key(self, entered_key: str) -> None:
        if self._get_key() != entered_key:
            raise ValueError("Wrong code phrase!")


class PasswordStorage:
    def __init__(self, db_file: str) -> None:
        self.db_file = db_file

    def read(self) -> dict[str, str]:
        with open(self.db_file, encoding='utf8') as file:
            res: dict[str, str] = json.load(file)
            return res

    def record(self, passwords: dict[str, str]) -> None:
        with open(self.db_file, 'w', encoding='utf8') as file:
            json.dump(passwords, file)


class BaseExporter:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name


class CsvExporter(BaseExporter):
    def __init__(self, file_name: str) -> None:
        super().__init__(file_name)

    def export(self, value: dict[str, str]) -> None:
        with open(self.file_name, 'w', encoding='utf8') as file:
            reader = csv.writer(file)
            for row in value.items():
                reader.writerow(row)


class JsonExporter(BaseExporter):
    def __init__(self, file_name: str) -> None:
        super().__init__(file_name)

    def export(self, value: dict[str, str]) -> None:
        with open(self.file_name, 'w', encoding='utf8') as file:
            json.dump(value, file)


class TxtExporter(BaseExporter):
    def __init__(self, file_name: str) -> None:
        super().__init__(file_name)

    def export(self, value: dict[str, str]) -> None:
        with open(self.file_name, 'w', encoding='utf8') as file:
            for identifier, password in value.items():
                file.write(f'{identifier}: {password}\n')


class ExcelExporter(BaseExporter):
    def __init__(self, file_name: str) -> None:
        super().__init__(file_name)

    def export(self, value: dict[str, str]) -> None:
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.append(['Identifier', "Password"])
        for key, password in value.items():
            worksheet.append([key, password])
        workbook.save(self.file_name)


class XmlExporter(BaseExporter):
    def __init__(self, file_name: str) -> None:
        super().__init__(file_name)

    def export(self, value: dict[str, str]) -> None:
        root = Et.Element('Passwords')
        for identifier, password in value.items():
            pas = Et.SubElement(root, 'password')
            pas.set('identifier', identifier)
            val = Et.SubElement(pas, 'value')
            val.text = password

        xml = minidom.parseString(Et.tostring(root)).toprettyxml(indent="  ")
        with open(self.file_name, 'w', encoding='utf8') as file:
            file.write(xml)
