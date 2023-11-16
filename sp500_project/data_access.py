import csv
import json
from interfaces import DbProto
from typing import TypeAlias
from DTO import CompanyDTO


CompaniesInfo: TypeAlias = list[CompanyDTO]


class Sp500Csv(DbProto):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def get_file_information(self) -> CompaniesInfo:
        with open(self.file_name, encoding='utf8') as file:
            res = []
            for row in csv.DictReader(file):
                res.append(CompanyDTO(symbol=row["Symbol"],
                                      name=row["Name"],
                                      sector=row["Sector"],
                                      price=float(row["Price"])))
            return res

    def record_new_line(self, new_line: CompanyDTO) -> None:
        new_info = {'Symbol': new_line.symbol,
                    'Name': new_line.name,
                    'Sector': new_line.sector,
                    'Price': new_line.price}
        headline = ['Symbol', 'Name', 'Sector', 'Price']
        with open(self.file_name, 'a', encoding='utf8') as new_file:
            writer = csv.DictWriter(new_file, fieldnames=headline)
            writer.writerow(new_info)

    def record_new_information(self, new_information: CompaniesInfo) -> None:
        new_info = []
        for company in new_information:
            new_info.append({'Symbol': company.symbol,
                             'Name': company.name,
                             'Sector': company.sector,
                             'Price': company.price})
        headline = ['Symbol', 'Name', 'Sector', 'Price']
        with open(self.file_name, 'w', encoding='utf8') as file:
            writer = csv.DictWriter(file, fieldnames=headline)
            writer.writeheader()
            writer.writerows(new_info)


class Sp500Json(DbProto):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def get_file_information(self) -> CompaniesInfo:
        with open(self.file_name, encoding='utf8') as file:
            res = []
            for row in json.load(file):
                res.append(CompanyDTO(symbol=row["Symbol"],
                                      name=row["Name"],
                                      sector=row["Sector"],
                                      price=row["Price"]))
            return res

    def record_new_line(self, new_line: CompanyDTO) -> None:
        data = self.get_file_information() + [new_line]
        res = []
        for company in data:
            res.append({'Symbol': company.symbol,
                        'Name': company.name,
                        'Sector': company.sector,
                        'Price': company.price})
        with open(self.file_name, 'w', encoding='utf8') as file:
            json.dump(res, file, indent=2)

    def record_new_information(self, new_information: CompaniesInfo) -> None:
        res = []
        for company in new_information:
            res.append({'Symbol': company.symbol,
                        'Name': company.name,
                        'Sector': company.sector,
                        'Price': company.price})
        with open(self.file_name, 'w', encoding='utf8') as file:
            json.dump(res, file, indent=2)
