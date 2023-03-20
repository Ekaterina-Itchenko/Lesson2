import json
from openpyxl import Workbook
from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def get_storage_info(self):
        raise NotImplementedError

    @abstractmethod
    def record_with_new_info(self, new_info: dict):
        raise NotImplementedError


class ICategories(ABC):
    @abstractmethod
    def get_all_categories(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def record_new_category(self, category, parameters):
        raise NotImplementedError


class IOrders(ABC):
    @abstractmethod
    def get_order_info(self):
        raise NotImplementedError

    @abstractmethod
    def record_order(self, order: dict):
        raise NotImplementedError

    @abstractmethod
    def read_file(self):
        raise NotImplementedError


class StorageJson(IStorage):
    def __init__(self, file_name):
        self.file_name = file_name

    def get_storage_info(self):
        with open(self.file_name, encoding='utf8') as file:
            return json.load(file)

    def record_with_new_info(self, new_info: dict):
        with open(self.file_name, 'w', encoding='utf8') as file:
            json.dump(new_info, file, indent=2, sort_keys=True)


class CategoriesJson(ICategories):
    def __init__(self, file_name):
        self.file_name = file_name

    def get_all_categories(self) -> dict:
        with open(self.file_name, encoding='utf8') as file:
            return json.load(file)

    def record_new_category(self, category, parameters):
        new_info = self.get_all_categories()
        new_info[category] = parameters
        with open(self.file_name, 'w', encoding='utf8') as file:
            json.dump(new_info, file, indent=2, sort_keys=True)


class OrdersJson(IOrders):
    def __init__(self, file_name):
        self.file_name = file_name

    def get_order_info(self):
        with open(self.file_name, encoding='utf8') as file:
            return json.load(file)

    def record_order(self, order: dict):
        if self.read_file():
            storage = self.get_order_info()
        else:
            storage = []
        with open(self.file_name, 'w', encoding='utf8') as file:
            storage.append(order)
            json.dump(storage, file, indent=2, sort_keys=True)

    def read_file(self):
        with open(self.file_name, encoding='utf8') as file:
            reader = file.read()
            if reader:
                return True
            else:
                return False


def record_to_exel_sheets(info1, info2, info3, info4):
    wb = Workbook()
    ws1 = wb.active
    ws1.title = 'Sheet1'
    for key in info1:
        ws1.append([key] + list(info1[key]))

    wb.create_sheet("Sheet2")
    ws2 = wb["Sheet2"]
    ws2.append(['Product name', 'Quantity of sold goods'])
    for key, value in info2.items():
        ws2.append([key[0], value])

    wb.create_sheet("Sheet3")
    ws3 = wb["Sheet3"]
    for order in info3:
        result = []
        for key, value in order.items():
            result.append(key)
            result.append(value)
        ws3.append(result)

    wb.create_sheet("Sheet4")
    ws4 = wb["Sheet4"]
    for key in info4:
        ws4.append([key] + [str(info4[key])])

    wb.save('statistic.xlsx')
