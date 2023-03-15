from random import uniform, randint
from faker import Faker
from time import time


cache = {}


def use_cache(live_time=10):
    def wrap(func):
        """Decorator for using cache"""

        def wrapper(*args, **kwargs):
            now = time()
            if args not in cache or now - cache[args][0] > live_time:
                value = func(*args, **kwargs)
                cache[args] = (now, value)
            return cache[args][1]

        return wrapper

    return wrap


@use_cache()
def find_info(text: str, db_connector) -> list:
    company_list = []
    for company_dict in db_connector.get_file_information():
        if text.lower() in company_dict.get('Name').lower():
            company_list.append(company_dict)
    return company_list


@use_cache()
def get_companies_by_sector(sector: str, db_connector) -> list:
    return list(filter(lambda comp: sector.lower() == comp['Sector'].lower(),
                       db_connector.get_file_information()))


def calculate_average_price(db_connector) -> float:
    total_price = 0
    for company_dict in db_connector.get_file_information():
        total_price += float(company_dict['Price'])
    return round(total_price /
                 len(db_connector.get_file_information()), 4)


def get_top_10_companies(db_connector) -> list:
    sorted_lst = sorted(db_connector.get_file_information(),
                        key=lambda dct: float(dct['Price']), reverse=True)
    return [(dct['Name'], dct['Price']) for dct in sorted_lst[:10]]


@use_cache()
def add_new_company(symbol, new_name, sector, price, db_connector):
    new_line = {'Symbol': symbol,
                'Name': new_name,
                'Sector': sector,
                'Price': price}
    db_connector.record_new_line(new_line)


@use_cache()
def update_company_name(symbol, new_name, db_connector):
    file = db_connector.get_file_information()
    for dct in file:
        if dct.get('Symbol').lower() == symbol.lower():
            dct['Name'] = new_name
    db_connector.record_new_information(file)


@use_cache()
def delete_company(symbol, db_connector):
    file = db_connector.get_file_information()
    for dct in file:
        if dct.get('Symbol').lower() == symbol.lower():
            index = file.index(dct)
            del file[index]
    db_connector.record_new_information(file)


def truncate_all(db_connector):
    file = []
    db_connector.record_new_information(file)


def take_random_symbol():
    letters_list = []
    fake = Faker()
    for _ in range(randint(3, 6)):
        letters_list.append(fake.random_uppercase_letter())
    return ''.join(letters_list)


@use_cache()
def generate_random_data(number, db_connector):
    new_information = []
    fake = Faker()
    for _ in range(int(number)):
        new_information.append({'Symbol': take_random_symbol(),
                                'Price': uniform(0, 1000),
                                'Name': fake.company(),
                                'Sector': fake.catch_phrase()})
    db_connector.record_new_information(new_information)
