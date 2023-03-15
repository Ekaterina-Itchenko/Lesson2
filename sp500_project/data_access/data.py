import csv
import json
from abc import ABC, abstractmethod


class FileDB(ABC):
    @abstractmethod
    def get_file_information(self):
        raise NotImplementedError

    @abstractmethod
    def record_new_line(self, new_line):
        raise NotImplementedError

    @abstractmethod
    def record_new_information(self, new_information):
        raise NotImplementedError


class Sp500Csv(FileDB):
    def __init__(self, file_name):
        self.file_name = file_name

    def get_file_information(self):
        with open(self.file_name, encoding='utf8') as file:
            return list(csv.DictReader(file))

    def record_new_line(self, new_line):
        with open(self.file_name, encoding='utf8') as file:
            headline = csv.DictReader(file).fieldnames
        with open(self.file_name, 'a', encoding='utf8') as new_file:
            writer = csv.DictWriter(new_file, fieldnames=headline)
            writer.writerow(new_line)

    def record_new_information(self, new_information: list):
        with open(self.file_name, encoding='utf8') as file:
            headline = csv.DictReader(file).fieldnames
        with open(self.file_name, 'w', encoding='utf8') as file:
            writer = csv.DictWriter(file, fieldnames=headline)
            writer.writeheader()
            writer.writerows(new_information)


class Sp500Json(FileDB):
    def __init__(self, file_name):
        self.file_name = file_name

    def get_file_information(self):
        with open(self.file_name, encoding='utf8') as file:
            return json.load(file)

    def record_new_line(self, new_line):
        data = self.get_file_information() + [new_line]
        with open(self.file_name, 'w', encoding='utf8') as file:
            json.dump(data, file, indent=2)

    def record_new_information(self, new_information: list):
        with open(self.file_name, 'w', encoding='utf8') as file:
            json.dump(new_information, file)
